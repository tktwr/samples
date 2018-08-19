#!/usr/bin/env python

import torch

def main():
    m = torch.load('mnist.model')
    print(m)

    for param in m.parameters():
        # 型を調べるとCPUかGPUかわかる。
        # CPU: torch.FloatTensor
        # GPU: torch.cuda.FloatTensor
        print(type(param.data))

if __name__ == '__main__':
    main()
