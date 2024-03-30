#!/usr/bin/env python

import torch

def main():
    m = torch.load('mnist.model')
    print("model:")
    print(m)

    print("params:")
    for param in m.parameters():
        # 型を調べるとCPUかGPUかわかる。
        # CPU: torch.FloatTensor
        # GPU: torch.cuda.FloatTensor
        print(type(param.data))
        print(param)

main()
