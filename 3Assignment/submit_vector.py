from client import submit, get_errors
from set_cur_state import get_current_state
from set_cur_state import set_current_state
overfit_state = [0.0, 0.1240317450077846, -6.211941063144333, 0.04933903144709126, 0.03810848157715883, 8.132366097133624e-05, -6.018769160916912e-05, -1.251585565299179e-07, 3.484096383229681e-08, 4.1614924993407104e-11, -6.732420176902565e-12]
current =[-0.011764667816203084, 7.623302419764887, -0.11006993149879493, 0.03830744531622357, 2.5054351141784756e-06, 1.3022781747267696e-08, -3.782240356612625e-07, -3.0249374857450915e-12, -8.883203577505152e-13, 1.7198939015974926e-12, 8.72161747382807e-14]
# submit('4wbRlSOEbHj0HmuzgNcnNc6KeW9ERzSsccXuswFyGlkn7bUMol', current)

x9 = [-0.011764667816203084, 7.623302419764887, -0.11006993149879493, 0.03830744531622357, 2.5054351141784756e-06, 1.3022781747267696e-08, -3.782240356612625e-07, -3.0249374857450915e-12, -8.883203577505152e-13, 1.7198939015974926e-12, 8.72161747382807e-14]
x6 = [-0.003413868520584271, -0.0035611317379478577, -0.0005980293816362071, 0.06474740456361705, -7.672814625772156e-07, -8.25319172483978e-06, -1.2228625502317498e-10, 1.1140113084776777e-08, 2.9908984261240654e-13, -4.199279071215726e-12, 1.7041628467008054e-16]
x1=[0.0010440405658062543, 0.00837160028936126, 0.020628696211702713, 0.04668840176170609, -4.747305001258025e-05, -8.914011402740157e-07, 2.7231960230485534e-09, -1.730196051881142e-10, -6.449456667692867e-13, 1.318803364102403e-12, -6.694109023918839e-16]
x2 = [-0.013189499556147179, 4.332497423978972e-05, -0.010647047422319436, 0.05057513101993012, 4.3225345192929085e-07, 1.43723549795222e-06, -2.6779962440273106e-10, 5.587258417949564e-10, -1.1090935197011036e-14, -1.831203112961714e-18, -3.252812603578735e-17]
x3 = [0.00011183833646082945, 4.1418793942196955e-06, 1.3584859018733395e-08, 0.037964268793103516, 1.991284803846684e-08, 1.5404433053820888e-11, -2.630517831283641e-10, -1.3753430137150746e-09, -6.816273529284959e-13, 2.3380564585884016e-12, -1.278177454773451e-15]
x4 = [-0.11617057653810625, 0.15859070684425736, -0.0028688051594403558, 0.028308868667992832, -1.3478708210366998e-07, 4.039807813621617e-06, -9.510042018468092e-10, -1.7551579351956197e-10, 5.135826895054351e-12, 2.2173315563500865e-12, -8.341716827583232e-15]
x5 = [-0.0011591129923836337, 0.12710714706711373, 0.006779213685410658, 0.048840624895722544, -3.1628826550441124e-05, 4.009719886261539e-06, -1.2682016395850108e-12, -2.4219481765926643e-12, -6.333812718280682e-15, -5.421010257283095e-14, 1.801988485388574e-17]
x7 = [2.4272016552597986e-14, -2.739814859627458e-15, -7.573712177117474e-09, 0.04912257238827522, -2.7586900245552502e-05, -2.135317843772574e-19, -8.748554103473011e-22, 1.5134710534384615e-09, 1.0656796634745274e-23, 7.082912915191764e-23, 1.6337749767875306e-23]
x8 = [-2.965939133371406e-06, 0.1012839854879407, -0.0004893794075181628, 0.04191959360747625, 1.3843798991525607e-06, -1.571411454897065e-08, 1.2386581938563264e-10, 2.8892468913793995e-09, -9.846492096198845e-15, 8.069655396274695e-15, -4.697879919794402e-16]
# state2 = [x3[x] for x in range(11)]
# err = get_errors('4wbRlSOEbHj0HmuzgNcnNc6KeW9ERzSsccXuswFyGlkn7bUMol', state2)
# print(err)
# print(err)

uf1 = [0.761126283252376, -0.08435412118963685, 0.001166404175803425, 0.010344988864286059, -4.139184887016429e-05, 1.2203492973664288e-06, -1.1747837920649265e-08, 7.247260029228446e-09, 2.326803636515952e-11, 9.859588323509848e-13, -1.0702458219702297e-14]
uf2 = [-0.35277667889728015, -0.9550009612906567, 0.00600839012438753, 0.008667072587624813, -1.2565343871983564e-05, 8.098502300195847e-06, -3.898281037169141e-07, 4.476476543942871e-09, -2.2219711751654855e-14, 1.0786361748016095e-12, 7.770457054834614e-14]


uf3 = [-0.019488384718226816, -0.0007340717594155497, 0.03221960291356588, -6.171229277306651e-05, 9.115343914645872e-06, 2.003037998981663e-06, -6.605194959602966e-08, 7.74480823178327e-09, -1.6780910165816536e-12, 1.7634850522679608e-12, -5.992454348596402e-16]

#**
uf4 = [-0.011764667816203084, 7.623302419764887, -0.11006993149879493, 0.03830744531622357, 2.5054351141784756e-06, 1.3022781747267696e-08, -3.782240356612625e-07, -3.0249374857450915e-12, -8.883203577505152e-13, 1.7198939015974926e-12, 8.72161747382807e-14]


x10 = [7.064545112112871, 0.9646636414612759, 0.15304513192484676, 0.16606159392027325, 1.6722411939751253e-13, 5.521683979641187e-15, -3.5807868026004527e-07, -1.1703468351414869e-15, -9.757020107512777e-16, 2.3975268729393533e-12, 3.5139373279441513e-14]
state =[x4, x3, uf4, uf1, x9]
set_current_state(state)
