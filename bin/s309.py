from utils import *
from amis import (
    get_model,
    encode,
    decode,
    deep_mutational_scan,
    compare,
    evolve,
    interpolate,
    extrapolate,
    reconstruct,
    reconstruct_prose,
)

def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description='S309 analysis')
    parser.add_argument('--namespace', type=str, default='s309',
                        help='Model namespace')
    parser.add_argument('--model-name', type=str, default='esm1b',
                        help='Type of language model (e.g., esm1b, esm-msa)')
    parser.add_argument('--lnorm', action='store_true', default=False,
                        help='Softmax length normalization')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()

    model = get_model(args)

    vh = (
        'QVQLVQSGAEVKKPGASVKVSCKASGYPFTSYGISWVRQAPGQGLEWMGWISTYNGNTNYAQKFQGRVTMTTDTSTTTGYMELRRLRSDDTAVYYCARDYTRGAWFGESLIGGFDNWGQGTLVTVSS'
    )
    vl = (
        'EIVLTQSPGTLSLSPGERATLSCRASQTVSSTSLAWYQQKPGQAPRLLIYGASSRATGIPDRFSGSGSGTDFTLTISRLEPEDFAVYYCQQHDTSLTFGGGTKVEIK'
    )

    new = reconstruct(vh, model, decode_kwargs={ 'exclude': 'unnatural' })
    compare(vh, new, namespace='S309 VH')
    print('')

    new = reconstruct(vl, model, decode_kwargs={ 'exclude': 'unnatural' })
    compare(vl, new, namespace='S309 VK')
