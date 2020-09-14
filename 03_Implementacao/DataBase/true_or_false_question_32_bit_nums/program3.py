>>> r.reverse("-110101101101001011111110011000")
"-000110011111110100101101101011"
>>> r.reverse("101011011001101010010111101100")
"001101111010010101100110110101"
>>> r.reverse(728147436)
634741827
>>> to_bits(0)
"0"
>>> to_bits(728147436)
"101011011001101010010111101100"
>>> binary_sum("101011011001101010010111101100"
               ,"10101001100001010111001111110")
"1000000100101110101010001101010"
>>> binary_sum("101011011001101010010111101100"
               ,"-1100001000110110110010110000100")
"-110101101101001011111110011000"
