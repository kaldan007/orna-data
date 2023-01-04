from pathlib import Path
from openpecha.utils import load_yaml, dump_yaml

def update_pagination(old_pagination, img_grp):
    new_pagination = old_pagination

    for uuid, ann in old_pagination['annotations'].items():
        img_num = ann['imgnum']
        reference = f"{img_grp}{int(img_num):04}"
        new_pagination['annotations'][uuid]['reference'] = reference

    return new_pagination

def get_image_grp(vol_id, meta):
    img_grp = meta['vol2fn'][vol_id][:-4]
    return img_grp

def update_paginations(pecha_id):
    pecha_path = Path(f"./editions_without_durchen/{pecha_id}/{pecha_id}.opf")
    meta = load_yaml((pecha_path / "meta.yml"))
    layer_dirs = list((pecha_path / "layers").iterdir())
    for layer_dir in layer_dirs:
        pagination_layer_path = layer_dir / "Pagination.yml"
        pagination_layer = load_yaml(pagination_layer_path)
        pagination_layer['local_ids'] = {}
        new_pagination = pagination_layer
        # img_grp = get_image_grp(layer_dir.stem, meta)
        # new_pagination = update_pagination(pagination_layer, img_grp)
        dump_yaml(new_pagination, pagination_layer_path)

if __name__ == "__main__":
    pecha_ids = [
        "I4DBEE949",
        "I8B1FB7BB",
        "I24F34903",
        "IA3E40644",
        "IC445E4EA",
        "IEA653111"
    ]
    for pecha_id in pecha_ids:
        update_paginations(pecha_id)

