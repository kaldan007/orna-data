from pathlib import Path
from openpecha.utils import load_yaml, dump_yaml


def fill_base_meta(old_meta, new_meta):
    for vol_id, img_grp in old_meta['vol2fn'].items():
        order = int(vol_id[1:])
        new_meta['bases'][vol_id] = {
            'source_metadata' : {},
            'order': order,
            'base_file': f"{vol_id}.txt",
            'statistics': {
                'ocr_word_median_confidence_index': 0.9999999,
                'ocr_word_mean_confidence_index': 0.9755740258134236
            }     
        }
    return new_meta


def update_meta(pecha_id):
    meta_path = Path(f"./editions_without_durchen/{pecha_id}/{pecha_id}.opf/meta.yml")
    old_meta = load_yaml(meta_path)
    new_meta = load_yaml(Path('./meta.yml'))
    new_meta = fill_base_meta(old_meta, new_meta)
    new_meta['id'] = pecha_id
    dump_yaml(new_meta, meta_path)

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
        update_meta(pecha_id)