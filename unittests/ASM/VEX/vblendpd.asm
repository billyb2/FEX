%ifdef CONFIG
{
  "HostFeatures": ["AVX"],
  "RegData": {
    "XMM2": ["0xAAAAAAAAAAAAAAAA", "0xCCCCCCCCCCCCCCCC", "0xEEEEEEEEEEEEEEEE", "0x9999999999999999"],
    "XMM3": ["0x1111111111111111", "0x3333333333333333", "0x5555555555555555", "0x7777777777777777"],
    "XMM4": ["0xAAAAAAAAAAAAAAAA", "0xCCCCCCCCCCCCCCCC", "0x0000000000000000", "0x0000000000000000"],
    "XMM5": ["0x1111111111111111", "0x3333333333333333", "0x0000000000000000", "0x0000000000000000"],
    "XMM6": ["0xAAAAAAAAAAAAAAAA", "0x3333333333333333", "0xEEEEEEEEEEEEEEEE", "0x7777777777777777"],
    "XMM7": ["0x1111111111111111", "0xCCCCCCCCCCCCCCCC", "0x5555555555555555", "0x9999999999999999"],
    "XMM8": ["0xAAAAAAAAAAAAAAAA", "0x3333333333333333", "0x0000000000000000", "0x0000000000000000"],
    "XMM9": ["0x1111111111111111", "0xCCCCCCCCCCCCCCCC", "0x0000000000000000", "0x0000000000000000"]
  },
  "MemoryRegions": {
    "0x100000000": "4096"
  }
}
%endif

lea rdx, [rel .data]

vmovapd ymm0, [rdx]
vmovapd ymm1, [rdx + 32]

; Selecting all of one input vector
vblendpd ymm2, ymm0, ymm1, 0    ; All of ymm0
vblendpd ymm3, ymm0, ymm1, 0xFF ; All of ymm1

vblendpd xmm4, xmm0, xmm1, 0    ; All of xmm0
vblendpd xmm5, xmm0, xmm1, 0xFF ; All of xmm1

; Alternating source vectors
vblendpd ymm6, ymm0, ymm1, 0b10101010
vblendpd ymm7, ymm0, ymm1, 0b01010101

vblendpd xmm8, xmm0, xmm1, 0b10101010
vblendpd xmm9, xmm0, xmm1, 0b01010101

hlt

align 32
.data:
dq 0xAAAAAAAAAAAAAAAA
dq 0xCCCCCCCCCCCCCCCC
dq 0xEEEEEEEEEEEEEEEE
dq 0x9999999999999999

dq 0x1111111111111111
dq 0x3333333333333333
dq 0x5555555555555555
dq 0x7777777777777777