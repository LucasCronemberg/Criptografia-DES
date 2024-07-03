
# Pesquisa Modelos DES, 3DES, Blowfish, AES, SAFER. Implementação DES (V1 -> PyCryptodome)

O Data Encryption Standard (DES) foi desenvolvido pela IBM nos anos 1970 e adotado pelo National Institute of Standards and Technology (NIST) como um padrão federal dos EUA em 1977. DES foi projetado para fornecer um nível elevado de segurança para dados confidenciais em uma era de crescente digitalização.
DES é um algoritmo de criptografia simétrica, o que significa que a mesma chave é usada tanto para criptografar quanto para descriptografar dados. DES opera em blocos de 64 bits de dados, transformando-os através de 16 rodadas de substituições e permutações complexas controladas por uma chave de 56 bits. Cada rodada envolve processos como expansão, substituição, permutação e chave XOR.
Embora DES fosse considerado seguro na época de sua adoção, a chave de 56 bits tornou-se um ponto fraco significativo com o avanço da capacidade computacional. Ataques de força bruta (testar todas as combinações possíveis de chaves) tornaram-se práticos, comprometendo a segurança do algoritmo. Em 1999, um grupo conseguiu quebrar uma chave DES em menos de um dia.
Devido às suas limitações de segurança, o uso de DES foi amplamente descontinuado em favor de algoritmos mais robustos. A introdução de Triple DES (3DES) e, posteriormente, do Advanced Encryption Standard (AES) foi uma resposta direta às vulnerabilidades do DES.


