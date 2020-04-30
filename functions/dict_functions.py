
def normalize_dict(d, sep):
    def transform(d, sep):
        nd = {}
        for k, v in d.items():
            if isinstance(v, dict):
                for kk, vv in v.items():
                    nd[f"{k}{sep}{kk}"] = vv
            else:
                nd[k] = v
        return nd

    keep_going = True
    nd = d
    while keep_going:
        nd = transform(nd, sep)
        for v in nd.values():
            if isinstance(v, dict):
                keep_going = True
                break
            else:
                keep_going = False

    for v in nd.values():
        if isinstance(v, list):
            for i in range(len(v)):
                if isinstance(v[i], dict):
                    v[i] = normalize_dict(v[i], sep)

    return nd


def normalize_dict_list(dl, sep):
    ndl = []
    for dx in dl:
        if isinstance(dx, dict):
            ndl.append(normalize_dict(dx, sep))
    return ndl
