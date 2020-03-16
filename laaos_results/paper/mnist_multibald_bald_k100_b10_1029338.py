store = {}
store['args']={'num_inference_samples': 100, 'available_sample_k': 10, 'initial_samples': [38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329], 'seed': 1029338, 'type': 'AcquisitionFunction.bald', 'acquisition_method': 'AcquisitionMethod.multibald', 'experiment_description': 'Reproduce b1, 5, 10 k10, 100 and default initial samples, no initial samples for all methods with BALD. (No culling!)', 'batch_size': 64, 'scoring_batch_size': 512, 'test_batch_size': 512, 'validation_set_size': 1024, 'early_stopping_patience': 3, 'epochs': 30, 'epoch_samples': 5056, 'target_accuracy': 0.96, 'target_num_acquired_samples': 300, 'log_interval': 20, 'min_remaining_percentage': 100, 'min_candidates_per_acquired_item': 20, 'dataset': 'DatasetEnum.mnist', 'experiment_task_id': 'mnist_multibald_bald_k100_b10_1029338', 'experiments_laaos': './experiment_configs/big_repro_b10_k100/configs.py', 'no_cuda': False, 'quickquick': False, 'initial_samples_per_class': 2, 'initial_percentage': 100, 'reduce_percentage': 0}
store['cmdline']=['./src/ignite_mnist.py', '--experiment_task_id=mnist_multibald_bald_k100_b10_1029338', '--experiments_laaos=./experiment_configs/big_repro_b10_k100/configs.py']
store['iterations']=[]
store['initial_samples']=[38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329]
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.6596, 'nll': 2.4499237154957654}, 'chosen_samples': [28957, 21443, 24497, 17371, 37440, 38898, 46613, 3795, 32678, 53954], 'chosen_samples_score': [1.1220635030016988, 2.0732028958023965, 2.8448193154726416, 3.4113186360426893, 3.8078774452155, 4.072236550078159, 4.2411777246279705, 4.368212710571117, 4.423385379504289, 4.466430277650765], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.903991749000852, 'batch_acquisition_elapsed_time': 85.71980380899913})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.6923, 'nll': 2.154152346356929}, 'chosen_samples': [17483, 1997, 18405, 37755, 27103, 56220, 15140, 24038, 19187, 9687], 'chosen_samples_score': [1.1260283063284438, 2.0896927145661506, 2.8707527117127776, 3.4521091266367963, 3.861089478162305, 4.120859473472939, 4.318762089550877, 4.443181684705717, 4.4692209847236395, 4.5335385314952585], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 9.668222160998994, 'batch_acquisition_elapsed_time': 84.34032102499987})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.7399, 'nll': 1.4594437354272607}, 'chosen_samples': [55064, 12445, 34610, 26563, 22579, 26358, 40198, 14357, 4679, 19369], 'chosen_samples_score': [1.007686227032274, 1.856045272943371, 2.5990493594911577, 3.1642302396468494, 3.581785713598748, 3.867058745653205, 4.103750188384659, 4.29279939145436, 4.364834231728463, 4.449046053169043], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 10.213546907001728, 'batch_acquisition_elapsed_time': 83.98880480300068})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.7464, 'nll': 1.420293783441663}, 'chosen_samples': [4767, 13109, 37632, 28469, 27209, 1812, 14623, 58394, 2634, 47132], 'chosen_samples_score': [0.963116120292327, 1.7521035170150507, 2.443886872868998, 3.0102092727877943, 3.443831410861235, 3.7640336096310616, 4.041344517078434, 4.176924037561869, 4.322636707615889, 4.401165922725108], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 10.122218074000557, 'batch_acquisition_elapsed_time': 84.84305725599916})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.7704, 'nll': 1.155147068605363}, 'chosen_samples': [43648, 34815, 7144, 57463, 31408, 17491, 25309, 7005, 43262, 40224], 'chosen_samples_score': [0.8628972106506198, 1.689920830236085, 2.3338919617407727, 2.885012854769085, 3.3186869159492627, 3.65660869879789, 3.905583796242426, 4.1097056612870855, 4.245602551386697, 4.304911701284717], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 9.498584077999112, 'batch_acquisition_elapsed_time': 84.82762711699979})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.8161, 'nll': 1.0983005435318947}, 'chosen_samples': [38892, 51679, 16073, 2381, 35230, 8480, 8676, 25960, 57336, 38409], 'chosen_samples_score': [1.0262222490373505, 1.9496055986097915, 2.733134138664133, 3.33151704532869, 3.7606590933339468, 4.071747179736912, 4.270809676323854, 4.344282696281903, 4.479000552266478, 4.542932123862426], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 11.837244921000092, 'batch_acquisition_elapsed_time': 84.51487007899777})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.8709, 'nll': 0.7975648690600992}, 'chosen_samples': [26132, 49543, 28987, 24485, 17494, 34608, 26072, 17756, 59468, 53976], 'chosen_samples_score': [0.9389680236146448, 1.8246923650059292, 2.585798640299269, 3.1966643440217597, 3.6315725583157006, 3.950874976080093, 4.15122726494256, 4.324793420325561, 4.39109266590679, 4.430654805574041], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 11.913108544998977, 'batch_acquisition_elapsed_time': 84.62426746300116})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.8753, 'nll': 0.7112136696571111}, 'chosen_samples': [32531, 58560, 35232, 19495, 8892, 33593, 22497, 42703, 48096, 34678], 'chosen_samples_score': [1.0004269244190993, 1.8786358099148868, 2.6531237476400915, 3.228093171661048, 3.65715895132361, 3.976996676048814, 4.1968690737076795, 4.331725191210035, 4.412784141562854, 4.434330765009276], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 11.487011015000462, 'batch_acquisition_elapsed_time': 84.59658544999911})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.8604, 'nll': 0.8355508643374445}, 'chosen_samples': [8763, 5175, 34886, 5842, 48507, 56190, 23452, 57506, 14650, 37773], 'chosen_samples_score': [0.876026222766644, 1.6817328856930356, 2.409549446804558, 3.029141236889897, 3.5105083889000253, 3.86427528033227, 4.104796192582232, 4.285798058051329, 4.405195048711914, 4.4594892694669666], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 11.988097023997398, 'batch_acquisition_elapsed_time': 84.00473295800111})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.8766, 'nll': 0.7497551240940094}, 'chosen_samples': [51371, 54004, 36152, 26733, 39818, 19824, 54880, 49890, 59626, 55496], 'chosen_samples_score': [0.9132817596921373, 1.73671975720444, 2.4660577345910375, 3.060021680793267, 3.5237569771029573, 3.859080044931769, 4.126109981383608, 4.252714213864637, 4.3639879558254915, 4.457553655835623], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 11.869292938998115, 'batch_acquisition_elapsed_time': 84.89268202699895})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.9069, 'nll': 0.6456060002550482}, 'chosen_samples': [7168, 1239, 1370, 8447, 11600, 12986, 45073, 11693, 48355, 50059], 'chosen_samples_score': [1.0102601833169798, 1.95710143992532, 2.7511580284479358, 3.386726340017713, 3.8430990076353706, 4.149007531090679, 4.346255702599456, 4.445679630142362, 4.50796438232833, 4.541784892484008], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 15.368861268998444, 'batch_acquisition_elapsed_time': 84.00786015999984})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.9066, 'nll': 0.6131010516502261}, 'chosen_samples': [3719, 20050, 28362, 27596, 43176, 14394, 44040, 9428, 26546, 52516], 'chosen_samples_score': [0.8360326307570135, 1.5637543252738877, 2.2095296396553907, 2.761575481411246, 3.227651121706661, 3.5873420833358383, 3.8361963494870857, 4.048798245641567, 4.234145048838682, 4.309091417169281], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 11.90648555900043, 'batch_acquisition_elapsed_time': 84.43353174399817})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.9268, 'nll': 0.5520506555301548}, 'chosen_samples': [33812, 32519, 13121, 12663, 50840, 34597, 9633, 14260, 33505, 53872], 'chosen_samples_score': [1.0659477015337377, 2.003734160116893, 2.803545594182003, 3.4423097926534556, 3.8808193697054465, 4.159861035423958, 4.32786550661228, 4.43665433227688, 4.48861020955793, 4.550962671419331], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 15.131869363001897, 'batch_acquisition_elapsed_time': 84.46286978400167})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.9239, 'nll': 0.5496715917598008}, 'chosen_samples': [38050, 14649, 9036, 26882, 36744, 42020, 11708, 30418, 32427, 49200], 'chosen_samples_score': [0.9561309729640441, 1.8426612773125846, 2.6185293746633787, 3.232895450989259, 3.6712956906785905, 3.966220489039648, 4.220072372934096, 4.378071961573641, 4.430676663479273, 4.453470198861533], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.575354881999374, 'batch_acquisition_elapsed_time': 84.67351162499835})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.9269, 'nll': 0.5506090934242606}, 'chosen_samples': [21426, 46412, 31301, 3056, 23486, 48006, 39411, 40752, 6944, 44095], 'chosen_samples_score': [0.9716018543643338, 1.8619750516512013, 2.651541612568352, 3.2802835318774135, 3.7200847900111143, 4.046799624396323, 4.265272063106905, 4.400382769427885, 4.465825409914606, 4.535549152387004], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.46569175300101, 'batch_acquisition_elapsed_time': 84.28779550499894})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.9256, 'nll': 0.5271029078235625}, 'chosen_samples': [54832, 32880, 36072, 24533, 15848, 11292, 8443, 35401, 50598, 53156], 'chosen_samples_score': [0.9138072003362322, 1.7705047591264949, 2.5211182462003747, 3.1508386023108783, 3.632565485403056, 3.9762742378765554, 4.182903124521694, 4.312957019180312, 4.425616780163695, 4.47478880053306], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.746898994999356, 'batch_acquisition_elapsed_time': 84.17234497199752})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.9212, 'nll': 0.5450175617600085}, 'chosen_samples': [55743, 20172, 32776, 24587, 55442, 52646, 42121, 27503, 19942, 38436], 'chosen_samples_score': [0.9910740549857056, 1.827337969416539, 2.5322451486876014, 3.1210394632790086, 3.565941196430521, 3.90748052886852, 4.133108476836381, 4.30329170960491, 4.396673319621017, 4.483612848752363], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.615824865999457, 'batch_acquisition_elapsed_time': 85.189291142})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.9215, 'nll': 0.5165046248552799}, 'chosen_samples': [1075, 57728, 24740, 6428, 38298, 18598, 16928, 1423, 29132, 4153], 'chosen_samples_score': [0.9097366887936084, 1.7183845848987245, 2.410145156761632, 2.989662279573932, 3.4437317051490997, 3.7937688813338895, 4.002263716575633, 4.159822022501657, 4.335335957719881, 4.395849264547538], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.382517625999753, 'batch_acquisition_elapsed_time': 84.0800872309992})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.9289, 'nll': 0.5266770734390614}, 'chosen_samples': [5600, 25803, 23927, 42209, 37403, 51993, 46368, 22591, 22083, 47220], 'chosen_samples_score': [0.9332370663435042, 1.7896276159944553, 2.5464060681346194, 3.1661971887811524, 3.6294273797089622, 3.9703511225140855, 4.191896796601059, 4.340605537717213, 4.38268768120143, 4.475594992471804], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 15.405733970001165, 'batch_acquisition_elapsed_time': 85.10724738499994})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.9425, 'nll': 0.45534945873945953}, 'chosen_samples': [59747, 17521, 48824, 7833, 19298, 13714, 3273, 47789, 45201, 6347], 'chosen_samples_score': [0.9419935941296936, 1.7678441558673172, 2.4995672837348204, 3.095501217299966, 3.5663318258643346, 3.8868200225482123, 4.128319807473034, 4.2837839543345355, 4.381804310370067, 4.463217976850882], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 15.456667531001585, 'batch_acquisition_elapsed_time': 83.97610610799893})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.9327, 'nll': 0.46008277098208666}, 'chosen_samples': [50317, 57718, 12066, 15855, 25300, 19524, 33162, 6418, 38082, 20641], 'chosen_samples_score': [1.0118515610082448, 1.9561706609951726, 2.762797144776993, 3.3759259954715457, 3.8113866347451957, 4.095744990334813, 4.297861086919732, 4.418630196510324, 4.507027307280711, 4.556880544288851], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 17.27533534199756, 'batch_acquisition_elapsed_time': 84.1859488730006})
store['iterations'].append({'num_epochs': 12, 'test_metrics': {'accuracy': 0.9456, 'nll': 0.4582423620923758}, 'chosen_samples': [36417, 37118, 47652, 37256, 13942, 34406, 26444, 14385, 43043, 48102], 'chosen_samples_score': [1.0651620143311513, 2.071353646284138, 2.9541716710394565, 3.5848560946272015, 4.01765589659545, 4.290113456393458, 4.41630618746612, 4.505438404959294, 4.555630635907194, 4.580478205170799], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 25.12223404299948, 'batch_acquisition_elapsed_time': 84.52713581999706})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.9474, 'nll': 0.44436057901531467}, 'chosen_samples': [24479, 36818, 34946, 9439, 10982, 7207, 56224, 14655, 43745, 5129], 'chosen_samples_score': [0.9077235993084812, 1.7631297777388646, 2.4973992049283416, 3.1215773851241897, 3.5831653454625476, 3.913049779812651, 4.149761202518409, 4.308149219991864, 4.399543452233421, 4.461769527564555], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 15.213555530997837, 'batch_acquisition_elapsed_time': 84.37234923099822})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.9457, 'nll': 0.44768207462632664}, 'chosen_samples': [45658, 49824, 55073, 49656, 9966, 36408, 52968, 59314, 18739, 7478], 'chosen_samples_score': [0.9667262200121518, 1.8656423002078057, 2.647481607161957, 3.279710801784741, 3.7403618109076313, 4.063975776260563, 4.229581172846469, 4.391791800307092, 4.453844948682231, 4.538837535984648], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 17.014727585999935, 'batch_acquisition_elapsed_time': 84.39644327499991})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.9501, 'nll': 0.3960177513805032}, 'chosen_samples': [9180, 11572, 39355, 31738, 20989, 4822, 20110, 19344, 35128, 2450], 'chosen_samples_score': [0.9304666543369712, 1.8055189339253672, 2.5716337855456497, 3.186969456041173, 3.6573149603379616, 3.970245169547315, 4.185740196588354, 4.304523694905935, 4.421544508738615, 4.514046540359215], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 18.94868813100038, 'batch_acquisition_elapsed_time': 84.38683676899745})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.9556, 'nll': 0.40677270677167177}, 'chosen_samples': [33222, 42078, 3648, 56643, 17849, 18324, 25192, 17747, 20036, 16834], 'chosen_samples_score': [0.8449048327687637, 1.6068240009612718, 2.2889862328152293, 2.854747670389925, 3.3146841270030127, 3.653666568398622, 3.9278887740219393, 4.10736011264199, 4.288132346765319, 4.364700343971166], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 15.552747575002286, 'batch_acquisition_elapsed_time': 84.11959812900022})
store['iterations'].append({'num_epochs': 10, 'test_metrics': {'accuracy': 0.9517, 'nll': 0.38184479363161333}, 'chosen_samples': [35246, 10044, 4185, 38920, 31184, 20183, 30900, 1674, 57276, 13729], 'chosen_samples_score': [1.037802611327046, 1.9827239293442969, 2.7880382817839293, 3.4292273816201755, 3.87685850776004, 4.147534339474875, 4.313924210045911, 4.467168530650432, 4.497056097330935, 4.524298613647931], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 20.636408556998504, 'batch_acquisition_elapsed_time': 84.48817288700229})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.9512, 'nll': 0.3983054984024763}, 'chosen_samples': [32276, 9118, 8268, 13031, 16911, 53736, 12254, 31046, 28632, 37048], 'chosen_samples_score': [1.099758890957789, 2.0208992521128097, 2.820655120840965, 3.428350192899183, 3.8437386506331275, 4.151541167644551, 4.32256227065395, 4.419760345197614, 4.4879984154209325, 4.514091210671742], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 19.015904570998828, 'batch_acquisition_elapsed_time': 84.4840100429974})