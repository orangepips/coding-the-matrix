from vec import Vec
from vecutil import list2vec
from GF2 import one

def lin_comb(vlist, clist):
    """

    :param vlist: list of vectors
    :param clist: list of scalars same length as vlist
    :return: linear combination of vectors in vlist with corresponding coeffecients in clist

    >>> D = {'metal','concrete','plastic','water','electricity'}
    >>> v_gnome = Vec(D,{'concrete':1.3,'plastic':.2,'water':.8,'electricity':.4})
    >>> v_hoop = Vec(D, {'plastic':1.5, 'water':.4, 'electricity':.3})
    >>> v_slinky = Vec(D, {'metal':.25, 'water':.2, 'electricity':.7})
    >>> v_putty = Vec(D, {'plastic':.3, 'water':.7, 'electricity':.5})
    >>> v_shooter = Vec(D, {'metal':.15, 'plastic':.5, 'water':.4,'electricity':.8})
    >>> v_combo = lin_comb([v_gnome, v_hoop, v_slinky, v_putty, v_shooter], [240, 55, 150, 133, 90])
    >>> v_combo == Vec(D,{'metal': 51.0, 'plastic': 215.4, 'electricity': 356.0, 'water': 373.1, 'concrete': 312.0})
    True
    >>> # 3.2.7
    >>> v_b1 = list2vec([one,one,one,0,0])
    >>> v_b2 = list2vec([0,one,one,one,0])
    >>> v_b3 = list2vec([0,0,one,one,one])
    >>> list2vec([one,0,one,0,one]) == lin_comb([v_b1, v_b2, v_b3], [one,one,one])
    True
    """
    assert isinstance(vlist, list)
    assert isinstance(clist, list)
    return sum([s*v for s, v in zip(clist, vlist)])