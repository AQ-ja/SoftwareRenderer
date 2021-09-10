from numpy.lib.arraysetops import unique
import MylibMath as Mlib


def flat(render, **kwargs):
    # Iluminacion se calcula por primitiva

    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    triangleNormal = kwargs['triangleNormal']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]
    intensity = Mlib.punto(triangleNormal, dirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def gourad(render, **kwargs):
    # Iluminacion por vertice, se interpola
    # la iluminacion por cada pixel
    
    u, v, w = kwargs['baryCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b/= 255
    g/= 255
    r/= 255

    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]
    intensityA = Mlib.punto(nA, dirLight)
    intensityB = Mlib.punto(nB, dirLight)
    intensityC = Mlib.punto(nC, dirLight)

    intensity = intensityA *u + intensityB *v + intensityC *w
    b*= intensity
    g*= intensity
    r*= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def phong(render, **kwargs):
    # Iluminacion por pixel
    
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]
    intensity = Mlib.punto(normal, dirLight)

    b*= intensity
    g*= intensity
    r*= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


# ¡¡¡¡¡¡ ACA EMPIEZAN MIS SHADERS   ¡¡¡¡¡¡¡¡¡¡¡


def tf(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    nA, nB, nC = kwargs['normals']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = nA[0] * u + nB[0] * v + nC[0] * w
    ny = nA[1] * u + nB[1] * v + nC[1] * w
    nz = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nx, ny, nz)
    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]

    intensity = Mlib.punto(normal, dirLight)

    if nx < 0:
        r = 1 - r
        b = 1 - b
        g = 1 - g

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def static(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    nA, nB, nC = kwargs['normals']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = nA[0] * u + nB[0] * v + nC[0] * w
    ny = nA[1] * u + nB[1] * v + nC[1] * w
    nz = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nx, ny, nz)
    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]

    intensity = Mlib.punto(normal, dirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def intense(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    nA, nB, nC = kwargs['normals']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = nA[0] * u + nB[0] * v + nC[0] * w
    ny = nA[1] * u + nB[1] * v + nC[1] * w
    nz = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nx, ny, nz)
    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]

    intensity = Mlib.punto(normal, dirLight)
    if intensity >0:
        if intensity > 0 and intensity < 0.25:
            intensity = 0.125
        elif intensity > 0.25 and intensity < 0.50:
            intensity = 0.375

        elif intensity > 0.50 and intensity <0.75:
            intensity = 0.625

        elif intensity > 0.75 and intensity <1:
            intensity = 0.875


    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0



def psyc(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    nA, nB, nC = kwargs['normals']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = nA[0] * u + nB[0] * v + nC[0] * w
    ny = nA[1] * u + nB[1] * v + nC[1] * w
    nz = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nx, ny, nz)

    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]

    intensity = Mlib.punto(normal, dirLight)
    if intensity >0:
        if intensity > 0.95:
            r *= 0.7 * intensity
        elif intensity > 0.9:
            g *= 0.7 * intensity
        elif intensity > 0.85:
            b *= 0.7 * intensity
        elif intensity > 0.8:
            r *= 0.5 * intensity

        elif intensity > 0.75:
            g *= 0.5 * intensity

        elif intensity > 0.7:
            b *= 0.5 * intensity

        elif intensity > 0.65:
            r *= 0.25 * intensity

        elif intensity > 0.6:
            g *= 0.25 * intensity

        elif intensity > 0.55:
            b *= 0.25 * intensity

        elif intensity > 0.5:
            r *= 0.12 * intensity

        elif intensity > 0.4:
            g *= 0.12 * intensity

        elif intensity > 0.3:
            b *= 0.12 * intensity

        elif intensity > 0.2:
            r *= 0.6 * intensity

        elif intensity > 0.1:
            g *= 0.6 * intensity

        elif intensity >= 0.0:
            b *= 0.6 * intensity
    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0





def neonish(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    nA, nB, nC = kwargs['normals']
    b, g, r = kwargs['color']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]
    intensity = Mlib.punto(normal, dirLight)

    dat1 = (0.2,0.5,0.8)
    dat2 = (0,0,0)

    if intensity > 0.90:
        r, g, b = dat1
    elif intensity > 0.80:
        r, g, b = dat2
    elif intensity > 0.70:
       r, g, b = dat1
    elif intensity > 0.60:
       r, g, b = dat2
    elif intensity > 0.50:
        r, g, b = dat2
    elif intensity > 0.40:
        r, g, b = dat2
    elif intensity > 0.30:
        r, g, b = dat2
    elif intensity > 0.20:
        r, g, b = dat2
    elif intensity > 0.10:
        r, g, b = dat2
    elif intensity > 0.01:
        r, g, b = dat2
    
    b*= intensity
    g*= intensity
    r*= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

    

def redish(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    nA, nB, nC = kwargs['normals']
    b, g, r = kwargs['color']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
       tx = tA[0] * u + tB[0] * v + tC[0] * w
       ty = tA[1] * u + tB[1] * v + tC[1] * w
       texColor = render.active_texture.getColor(tx, ty)
       b *= texColor[0] / 255
       g *= texColor[1] / 255
       r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]
    intensity = Mlib.punto(dirLight, normal)

    dat1 = (1,1,1)
    dat2 = (0.1,0.1,0.1)

    if intensity > 1:
        r, g, b = dat1
    elif intensity > 0.99:
        r, g, b = dat1
    elif intensity > 0.98:
        r, g, b = dat2
    elif intensity > 0.97:
        r, g, b = dat1
    elif intensity > 0.96:
        r, g, b = dat2
    elif intensity > 0.95:
        r, g, b = dat1
    elif intensity > 0.94:
        r, g, b = dat2
    elif intensity > 0.93:
        r, g, b = dat1
    elif intensity > 0.92:
        r, g, b = dat2
    elif intensity > 0.91:
        r, g, b = dat1
    elif intensity > 0.90:
        r, g, b = dat2
    elif intensity > 0.89:
        r, g, b = dat2
    elif intensity > 0.88:
        r, g, b = dat1
    elif intensity > 0.87:
        r, g, b = dat2
    elif intensity > 0.86:
        r, g, b = dat1
    elif intensity > 0.85:
        r, g, b = dat2
    elif intensity > 0.84:
        r, g, b = dat1
    elif intensity > 0.83:
        r, g, b = dat2
    elif intensity > 0.82:
        r, g, b = dat1
    elif intensity > 0.81:
        r, g, b = dat2
    elif intensity > 0.80:
        r, g, b = dat2
    elif intensity > 0.79:
        r, g, b = dat1
    elif intensity > 0.78:
        r, g, b = dat2
    elif intensity > 0.77:
        r, g, b = dat1
    elif intensity > 0.76:
        r, g, b = dat2
    elif intensity > 0.75:
        r, g, b = dat1
    elif intensity > 0.74:
        r, g, b = dat2
    elif intensity > 0.73:
        r, g, b = dat1
    elif intensity > 0.72:
        r, g, b = dat2
    elif intensity > 0.71:
        r, g, b = dat2
    elif intensity > 0.70:
        r, g, b = dat1
    elif intensity > 0.69:
        r, g, b = dat2
    elif intensity > 0.68:
        r, g, b = dat1
    elif intensity > 0.67:
        r, g, b = dat2
    elif intensity > 0.66:
        r, g, b = dat1
    elif intensity > 0.65:
        r, g, b = dat2
    elif intensity > 0.64:
        r, g, b = dat1
    elif intensity > 0.63:
        r, g, b = dat2
    elif intensity > 0.62:
        r, g, b = dat2
    elif intensity > 0.61:
        r, g, b = dat1
    elif intensity > 0.60:
        r, g, b = dat2
    elif intensity > 0.59:
        r, g, b = dat1
    elif intensity > 0.58:
        r, g, b = dat2
    elif intensity > 0.57:
        r, g, b = dat1
    elif intensity > 0.56:
        r, g, b = dat2
    elif intensity > 0.55:
        r, g, b = dat1
    elif intensity > 0.54:
        r, g, b = dat2
    elif intensity > 0.53:
        r, g, b = dat2
    elif intensity > 0.52:
        r, g, b = dat1
    elif intensity > 0.51:
        r, g, b = dat2
    elif intensity > 0.50:
        r, g, b = dat1
    elif intensity > 0.49:
        r, g, b = dat2
    elif intensity > 0.48:
        r, g, b = dat1
    elif intensity > 0.47:
        r, g, b = dat2
    elif intensity > 0.46:
        r, g, b = dat1
    elif intensity > 0.45:
        r, g, b = dat2
    elif intensity > 0.44:
        r, g, b = dat2
    elif intensity > 0.43:
        r, g, b = dat1
    elif intensity > 0.42:
        r, g, b = dat2
    elif intensity > 0.41:
        r, g, b = dat1
    elif intensity > 0.40:
        r, g, b = dat2
    elif intensity > 0.39:
        r, g, b = dat1
    elif intensity > 0.38:
        r, g, b = dat2
    elif intensity > 0.37:
        r, g, b = dat1
    elif intensity > 0.36:
        r, g, b = dat2
    elif intensity > 0.35:
        r, g, b = dat2
    elif intensity > 0.34:
        r, g, b = dat1
    elif intensity > 0.33:
        r, g, b = dat2
    elif intensity > 0.32:
        r, g, b = dat1
    elif intensity > 0.31:
        r, g, b = dat2
    elif intensity > 0.30:
        r, g, b = dat1
    elif intensity > 0.29:
        r, g, b = dat2
    elif intensity > 0.28:
        r, g, b = dat1
    elif intensity > 0.27:
        r, g, b = dat2
    elif intensity > 0.26:
        r, g, b = dat2
    elif intensity > 0.25:
        r, g, b = dat1
    elif intensity > 0.24:
        r, g, b = dat2
    elif intensity > 0.23:
        r, g, b = dat1
    elif intensity > 0.22:
        r, g, b = dat2
    elif intensity > 0.21:
        r, g, b = dat1
    elif intensity > 0.20:
        r, g, b = dat2
    elif intensity > 0.19:
        r, g, b = dat1
    elif intensity > 0.18:
        r, g, b = dat2
    elif intensity > 0.17:
        r, g, b = dat2
    elif intensity > 0.16:
        r, g, b = dat1
    elif intensity > 0.15:
        r, g, b = dat2
    elif intensity > 0.14:
        r, g, b = dat1
    elif intensity > 0.13:
        r, g, b = dat2
    elif intensity > 0.12:
        r, g, b = dat1
    elif intensity > 0.11:
        r, g, b = dat2
    elif intensity > 0.10:
        r, g, b = dat1
    elif intensity > 0.9:
        r, g, b = dat2
    elif intensity > 0.8:
        r, g, b = dat2
    elif intensity > 0.7:
        r, g, b = dat1
    elif intensity > 0.6:
        r, g, b = dat2
    elif intensity > 0.5:
        r, g, b = dat1
    elif intensity > 0.4:
        r, g, b = dat2
    elif intensity > 0.3:
        r, g, b = dat1
    elif intensity > 0.2:
        r, g, b = dat2
    elif intensity > 0.1:
        r, g, b = dat1
    elif intensity > 0.0:
        r, g, b = dat2
    """   
    elif intensity > 0.49:
        r, g, b = dat1[0]
    elif intensity > 0.40:
        r, g, b = dat2[0]
    elif intensity > 0.39:
        r, g, b = dat1[1]
    elif intensity > 0.30:
        r, g, b = dat2[0]
    elif intensity > 0.29:
        r, g, b = dat1[1]
    elif intensity > 0.20:
        r, g, b = dat2[0]
    elif intensity > 0.19:
        r, g, b = dat1[0]
    elif intensity > 0.10:
        r, g, b = dat2[1]
    elif intensity > 0.01:
        r, g, b = dat2[0]
"""
    b*= intensity
    g*= intensity
    r*= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

        



def dotish(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    nA, nB, nC = kwargs['normals']
    b, g, r = kwargs['color']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]
    intensity = Mlib.punto(normal, dirLight)

    dat1 = (1,1,1)
    dat2 = (0.5,0.3,0.2)
    dat3 = (0, 0, 0)

    if intensity >= 0.99:
        r, g, b = dat1
    elif intensity > 0.95:
        r, g, b = dat3
    elif intensity > 0.90:
        r, g, b = dat2
    elif intensity > 0.89:
        r, g, b = dat1
    elif intensity > 0.85:
        r, g, b = dat3
    elif intensity > 0.80:
        r, g, b = dat2
    elif intensity > 0.79:
        r, g, b = dat1
    elif intensity > 0.75:
        r, g, b = dat3
    elif intensity > 0.70:
        r, g, b = dat2
    elif intensity > 0.69:
        r, g, b = dat1
    elif intensity > 0.65:
        r, g, b = dat3
    elif intensity > 0.60:
        r, g, b = dat2
    elif intensity > 0.59:
        r, g, b = dat1
    elif intensity > 0.55:
        r, g, b = dat3
    elif intensity > 0.50:
       r, g, b = dat1
    elif intensity > 0.49:
        r, g, b = dat1
    elif intensity > 0.45:
        r, g, b = dat3
    elif intensity > 0.40:
        r, g, b = dat2
    elif intensity > 0.39:
        r, g, b = dat1
    elif intensity > 0.35:
        r, g, b = dat3
    elif intensity > 0.30:
        r, g, b = dat2
    elif intensity > 0.29:
        r, g, b = dat1
    elif intensity > 0.25:
        r, g, b = dat3
    elif intensity > 0.20:
        r, g, b = dat2
    elif intensity > 0.19:
        r, g, b = dat1
    elif intensity > 0.15:
        r, g, b = dat3
    elif intensity > 0.10:
        r, g, b = dat2
    elif intensity > 0.05:
        r, g, b = dat3
    elif intensity > 0.01:
        r, g, b = dat2



    b*= intensity
    g*= intensity
    r*= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0






def unlit(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    return r, g, b


def toon(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]
    intensity = Mlib.punto(normal, dirLight)

    if intensity > 0.7:
        intensity = 1
    elif intensity > 0.3:
        intensity = 0.5
    else:
        intensity = 0.05


    b*= intensity
    g*= intensity
    r*= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def textureBlend(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]
    intensity = Mlib.punto(normal, dirLight)

    if intensity < 0:
        intensity = 0

    b*= intensity
    g*= intensity
    r*= intensity

    if render.active_texture2:
        texColor = render.active_texture2.getColor(tx, ty)
        b += (texColor[0] / 255) * (1 - intensity)
        g += (texColor[1] / 255) * (1 - intensity)
        r += (texColor[2] / 255) * (1 - intensity)


    return r, g, b