store = {}
store['args']={'num_inference_samples': 10, 'available_sample_k': 10, 'seed': 289629, 'type': 'AcquisitionFunction.variation_ratios', 'acquisition_method': 'AcquisitionMethod.independent', 'experiment_description': 'RMNIST with noise k100 var ratios and mean stddev', 'initial_samples': [38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329], 'batch_size': 64, 'scoring_batch_size': 512, 'test_batch_size': 512, 'validation_set_size': 3072, 'early_stopping_patience': 3, 'epochs': 40, 'epoch_samples': 5056, 'target_accuracy': 0.95, 'target_num_acquired_samples': 300, 'initial_percentage': 100, 'reduce_percentage': 0, 'min_remaining_percentage': 100, 'min_candidates_per_acquired_item': 100, 'log_interval': 20, 'dataset': 'DatasetEnum.repeated_mnist_w_noise', 'experiment_task_id': 'rmnist_w_noise_independent_variation_ratios_k10_b10_289629', 'experiments_laaos': './experiment_configs/rmnist_w_noise_other_methods/configs.py', 'no_cuda': False, 'quickquick': False, 'initial_samples_per_class': 2, 'balanced_validation_set': False}
store['cmdline']=['./src/ignite_mnist.py', '--experiment_task_id=rmnist_w_noise_independent_variation_ratios_k10_b10_289629', '--experiments_laaos=./experiment_configs/rmnist_w_noise_other_methods/configs.py']
store['iterations']=[]
store['initial_samples']=[38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329]
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.6393, 'nll': 2.7150498905593157}, 'chosen_samples': [127448, 7448, 13912, 2593, 67448, 52303, 32266, 140328, 80532, 34597], 'chosen_samples_score': [0.8150750792653463, 0.8129303673068181, 0.8108509557388534, 0.8046053204657511, 0.8020222593441048, 0.8008317145595177, 0.8003096701882708, 0.7988342930288337, 0.7975162773392767, 0.7959797258324126], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 12.621450634000212, 'batch_acquisition_elapsed_time': 39.42789426300078})
store['iterations'].append({'num_epochs': 11, 'test_metrics': {'accuracy': 0.7291, 'nll': 3.168980137037039}, 'chosen_samples': [96825, 36825, 156825, 93802, 153802, 33802, 97870, 103208, 132378, 60418], 'chosen_samples_score': [0.8350145922307038, 0.8283783046932212, 0.8241893497822231, 0.8161431614690454, 0.8151197741908447, 0.8149400154065575, 0.8090488042572086, 0.8063255081534524, 0.8049304129675123, 0.8045827548665404], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 23.608419786000013, 'batch_acquisition_elapsed_time': 41.41043310299938})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.709, 'nll': 2.3119202716457843}, 'chosen_samples': [72787, 148424, 169090, 133766, 109090, 12787, 41283, 120680, 8440, 114048], 'chosen_samples_score': [0.8015841489991951, 0.8005733972818804, 0.8005645080038359, 0.799652469446753, 0.7986540340545659, 0.7975141765672573, 0.796812474502822, 0.7962716749452292, 0.7955401312598519, 0.7953131637549552], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 12.108751479001512, 'batch_acquisition_elapsed_time': 39.234399465000024})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.7684, 'nll': 1.802498088814616}, 'chosen_samples': [44255, 164255, 54836, 114836, 16756, 102515, 148717, 61937, 162515, 36375], 'chosen_samples_score': [0.7972274062522213, 0.7948237935469304, 0.7907955418619275, 0.7905935372249002, 0.789925735206821, 0.786224337089986, 0.7857264784554243, 0.7853605146188127, 0.784184007059257, 0.7832950971697622], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 11.269979648001026, 'batch_acquisition_elapsed_time': 39.09465394200015})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.8067, 'nll': 1.7737639133137466}, 'chosen_samples': [150077, 30077, 90077, 125315, 15191, 5315, 135191, 75191, 97926, 65315], 'chosen_samples_score': [0.8142441000178892, 0.8097160711571555, 0.8043820732846394, 0.7871628536534966, 0.7856304467286818, 0.785006799050727, 0.7823220973479477, 0.7809522302179032, 0.7745385089797475, 0.7731447899773571], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 18.35651123000207, 'batch_acquisition_elapsed_time': 39.12176565700065})
store['iterations'].append({'num_epochs': 11, 'test_metrics': {'accuracy': 0.8108, 'nll': 2.022907595745325}, 'chosen_samples': [80692, 20692, 140692, 116472, 176472, 43588, 24508, 103588, 163588, 89300], 'chosen_samples_score': [0.7999926531799315, 0.7955513635253618, 0.7942138821032675, 0.7899014184203983, 0.7864549713236948, 0.7847003652496333, 0.7845737436493088, 0.7837805151649655, 0.783372840141258, 0.7820586403804124], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 21.648376685003313, 'batch_acquisition_elapsed_time': 39.56020487799833})
store['iterations'].append({'num_epochs': 11, 'test_metrics': {'accuracy': 0.8061, 'nll': 2.0387886732017995}, 'chosen_samples': [155624, 51066, 110433, 171066, 169524, 170433, 50433, 111066, 172894, 94872], 'chosen_samples_score': [0.8158434872371711, 0.8098460834812402, 0.8049334703999886, 0.8032572735731751, 0.7966317423896939, 0.7917353836048128, 0.7912419467283336, 0.7784508292555175, 0.7775703996103225, 0.775169688228625], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 22.83830675900026, 'batch_acquisition_elapsed_time': 39.35239791099957})
store['iterations'].append({'num_epochs': 15, 'test_metrics': {'accuracy': 0.837, 'nll': 1.6233790548050404}, 'chosen_samples': [115425, 6832, 55425, 83423, 11464, 175425, 117302, 131464, 101180, 5035], 'chosen_samples_score': [0.7871628566838567, 0.7864138360751219, 0.7822506049062854, 0.778215372388163, 0.7731317851518085, 0.7724627226294931, 0.7706973955076138, 0.7700451905767943, 0.7700288462637821, 0.7650640929961245], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 29.83445402200232, 'batch_acquisition_elapsed_time': 39.693225756000174})
store['iterations'].append({'num_epochs': 10, 'test_metrics': {'accuracy': 0.8627, 'nll': 1.1985904763174058}, 'chosen_samples': [69559, 149334, 89334, 42153, 102333, 102329, 132836, 43226, 1032, 16379], 'chosen_samples_score': [0.7915411820744274, 0.7894807975523922, 0.7889330331975244, 0.7854611424588479, 0.7823845479989415, 0.7821778136114009, 0.7777915589101241, 0.77226577514392, 0.7722256883644009, 0.771673179927694], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 20.84692866000114, 'batch_acquisition_elapsed_time': 39.57774291699752})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.8474, 'nll': 1.0576782566308978}, 'chosen_samples': [174406, 156528, 20824, 832, 1140, 96528, 54406, 114406, 80824, 163192], 'chosen_samples_score': [0.804087902911851, 0.8018297187773059, 0.800658547726569, 0.7989180424154406, 0.7963909043343702, 0.7962010887383402, 0.7958944340675893, 0.7955556100120478, 0.7939836866680532, 0.7885104113080962], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.530729386999155, 'batch_acquisition_elapsed_time': 40.90793879099874})
store['iterations'].append({'num_epochs': 13, 'test_metrics': {'accuracy': 0.9007, 'nll': 1.0415140253102781}, 'chosen_samples': [107445, 5063, 143824, 125063, 76164, 83824, 16164, 8887, 167445, 65063], 'chosen_samples_score': [0.7802847350759395, 0.7795140931430566, 0.7789402827222219, 0.7770505532511703, 0.7768380375674597, 0.7684849023373815, 0.7662317375789305, 0.7640845901426108, 0.759635811612562, 0.7580672478512874], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 26.6740250820003, 'batch_acquisition_elapsed_time': 41.94560638900293})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.8858, 'nll': 0.9973000964164734}, 'chosen_samples': [122588, 144424, 100720, 143136, 4700, 84424, 40720, 20989, 120246, 97397], 'chosen_samples_score': [0.7886247409471924, 0.7885012336430506, 0.7854580716806785, 0.783777221534026, 0.7820362214874909, 0.7818107905935527, 0.779044498083315, 0.7788705167571843, 0.7785623392355415, 0.7777114776851601], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 16.58637237900257, 'batch_acquisition_elapsed_time': 39.58807411399903})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.8832, 'nll': 0.9196061454856396}, 'chosen_samples': [59312, 179312, 119312, 157704, 153197, 33197, 36573, 169140, 176813, 121888], 'chosen_samples_score': [0.8187279906428889, 0.8110965615292264, 0.8105982640283805, 0.8035733627561653, 0.8025325356352372, 0.7995173580662268, 0.7883898293402013, 0.7800671914884165, 0.7759137336879858, 0.7747979521309514], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 15.342583074998402, 'batch_acquisition_elapsed_time': 41.69267772299645})
store['iterations'].append({'num_epochs': 11, 'test_metrics': {'accuracy': 0.8965, 'nll': 0.9299525296700002}, 'chosen_samples': [31717, 164494, 91717, 140942, 48352, 167473, 73805, 80942, 167020, 108352], 'chosen_samples_score': [0.8116483384650239, 0.791709273788517, 0.784278046664199, 0.7794007480011556, 0.774434655798877, 0.7729922771042397, 0.7722740436270457, 0.7711617109286, 0.769688089920178, 0.7689493423529741], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 22.591852020996157, 'batch_acquisition_elapsed_time': 38.997588930003985})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.8987, 'nll': 0.8036912283563615}, 'chosen_samples': [150542, 14785, 30542, 107321, 69279, 171614, 51614, 90542, 9279, 129279], 'chosen_samples_score': [0.7973151004159018, 0.7963214170487269, 0.788954848751689, 0.7813405677657289, 0.77410208411534, 0.7738193733564945, 0.7737822359183743, 0.7736024088617339, 0.7734188026039233, 0.7727256307417404], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 16.915426633997413, 'batch_acquisition_elapsed_time': 38.52827308400447})
store['iterations'].append({'num_epochs': 14, 'test_metrics': {'accuracy': 0.9023, 'nll': 1.0031188285422323}, 'chosen_samples': [32880, 39265, 120340, 156934, 44948, 152079, 159265, 104948, 8883, 84623], 'chosen_samples_score': [0.779531922710271, 0.7767810288634728, 0.7728450312805157, 0.7713953017741936, 0.7712298148544554, 0.769892173378822, 0.7684181797371992, 0.7673235534745966, 0.7671585208103923, 0.7651327269837214], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 28.45998781399976, 'batch_acquisition_elapsed_time': 38.83011688899569})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.9149, 'nll': 0.7044982056838276}, 'chosen_samples': [53873, 113873, 173873, 143462, 38080, 158080, 63598, 116006, 105490, 3598], 'chosen_samples_score': [0.8021503320701637, 0.8011041417637816, 0.7905915545900207, 0.7882849044967133, 0.780741135487083, 0.7766438979253268, 0.7652129614227592, 0.7627249166988823, 0.7621776578732009, 0.7621706588322739], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 18.723574166993785, 'batch_acquisition_elapsed_time': 40.84280217400374})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.9238, 'nll': 0.7136411707437037}, 'chosen_samples': [6818, 126818, 66818, 71992, 39818, 99818, 21356, 32032, 75771, 147241], 'chosen_samples_score': [0.7927264338576516, 0.7860696064826049, 0.7831716660946204, 0.7650898438496292, 0.7648994982460686, 0.7618549838167762, 0.7611094869604227, 0.7602918012004855, 0.7594008139081254, 0.7592301936554612], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 18.822291177995794, 'batch_acquisition_elapsed_time': 40.21646957399935})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.915, 'nll': 0.6626721906805038}, 'chosen_samples': [81066, 94410, 141066, 175488, 153358, 34410, 140709, 123626, 154410, 63626], 'chosen_samples_score': [0.7920125030272631, 0.7864415601057856, 0.7827979668453426, 0.7812792867293017, 0.7796950407831206, 0.7796463108171928, 0.7789246894111872, 0.7768422840456574, 0.7767759452242747, 0.7746098672766222], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 16.381354470002407, 'batch_acquisition_elapsed_time': 40.271894706995226})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.9145, 'nll': 0.6813213044881822}, 'chosen_samples': [170368, 50368, 139507, 146588, 114542, 54542, 110368, 19507, 169488, 177076], 'chosen_samples_score': [0.7824188800693836, 0.7782619639384483, 0.7766450332012124, 0.7743826068322812, 0.7738758422700494, 0.7737208652240676, 0.7715929645175035, 0.7682701940065595, 0.768185190888462, 0.766645110672347], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 14.91484899399802, 'batch_acquisition_elapsed_time': 39.50254986000073})
store['iterations'].append({'num_epochs': 10, 'test_metrics': {'accuracy': 0.9278, 'nll': 0.6783644829767943}, 'chosen_samples': [67984, 136376, 76376, 127984, 7984, 48507, 17663, 146733, 77663, 147673], 'chosen_samples_score': [0.7819811584227188, 0.7816138575467286, 0.7769232797828132, 0.767757051792149, 0.7673494681418538, 0.7622007284222481, 0.7615125237926059, 0.760888418256811, 0.7595022956007339, 0.756386425591652], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 20.683556798998325, 'batch_acquisition_elapsed_time': 40.42164070400031})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.9274, 'nll': 0.5531229974496364}, 'chosen_samples': [110224, 50224, 170224, 135108, 58398, 83486, 118398, 15108, 178398, 162526], 'chosen_samples_score': [0.8280006972104696, 0.8209901407451985, 0.820274505196402, 0.7969747411629724, 0.7954674039364448, 0.7928723806931396, 0.7862314394299315, 0.7860376719471878, 0.7848610484886422, 0.7838145382256404], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.09877295500337, 'batch_acquisition_elapsed_time': 39.69236145100149})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.9268, 'nll': 0.5585041989064216}, 'chosen_samples': [74500, 98316, 158316, 14500, 134500, 38316, 71536, 131536, 101416, 26745], 'chosen_samples_score': [0.8217255090607346, 0.8195409605870467, 0.8181425526153987, 0.8152225233026641, 0.8139077460417836, 0.8135356498264121, 0.7968374541224235, 0.7959747787846604, 0.7883648512758887, 0.7866120437807963], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 12.944253540001228, 'batch_acquisition_elapsed_time': 40.94719258200348})
store['iterations'].append({'num_epochs': 11, 'test_metrics': {'accuracy': 0.937, 'nll': 0.5513106392884253}, 'chosen_samples': [162953, 116014, 42953, 176014, 102953, 41897, 28080, 148080, 112163, 171144], 'chosen_samples_score': [0.7833981127256194, 0.7815999832381316, 0.7754091746834657, 0.7693133697390921, 0.7684194689215134, 0.7666746324040884, 0.7631932865376791, 0.7610223198284988, 0.7597864755576575, 0.7596635848752216], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 23.18093810299615, 'batch_acquisition_elapsed_time': 39.757398419998935})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.9407, 'nll': 0.5256709031230212}, 'chosen_samples': [87406, 53170, 109895, 81024, 113170, 166132, 46132, 16045, 163206, 106132], 'chosen_samples_score': [0.7762382970989455, 0.7748460478383354, 0.7727131386982102, 0.7694072441654284, 0.769381314810727, 0.7687070581966358, 0.7680358213972704, 0.7669539707702403, 0.763396305711313, 0.7633172093676147], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 17.15162508100184, 'batch_acquisition_elapsed_time': 39.38357984100003})
store['iterations'].append({'num_epochs': 10, 'test_metrics': {'accuracy': 0.9377, 'nll': 0.5676100272941589}, 'chosen_samples': [54082, 114082, 136467, 174082, 97178, 16467, 10446, 157178, 76467, 63034], 'chosen_samples_score': [0.8017560158630509, 0.791969155670852, 0.7895511006760316, 0.7843492166257151, 0.7756298717813794, 0.7745449849411663, 0.769385812187994, 0.7644562629252136, 0.7640269108176688, 0.7617910675899081], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 19.645631672996387, 'batch_acquisition_elapsed_time': 42.056387302000076})
store['iterations'].append({'num_epochs': 10, 'test_metrics': {'accuracy': 0.9414, 'nll': 0.47716618308186526}, 'chosen_samples': [113158, 104157, 167012, 154899, 68674, 164157, 45439, 44157, 12812, 43906], 'chosen_samples_score': [0.7666311041206878, 0.7634767499784827, 0.760028218394837, 0.7588951572960129, 0.7565578827120346, 0.7558653527134882, 0.7558625158025477, 0.7546576082343966, 0.7542096694021125, 0.7538450042765169], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 20.199704127000587, 'batch_acquisition_elapsed_time': 38.5486844449988})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.9468, 'nll': 0.44464137449800967}, 'chosen_samples': [37363, 157363, 54883, 31413, 97363, 49525, 114883, 174883, 151415, 121075], 'chosen_samples_score': [0.7990751130498891, 0.7849258827725101, 0.7796267919377463, 0.7791936755432939, 0.7774647463851074, 0.7741887127113607, 0.7738074312381957, 0.7734423126436295, 0.7702356892890894, 0.7666262300625651], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 14.419145104002382, 'batch_acquisition_elapsed_time': 39.39731010400283})
store['iterations'].append({'num_epochs': 11, 'test_metrics': {'accuracy': 0.9381, 'nll': 0.5942614849650861}, 'chosen_samples': [35246, 59726, 155246, 119726, 179726, 151014, 4066, 109088, 91014, 64066], 'chosen_samples_score': [0.7958709858832915, 0.7946346883576854, 0.7880895651652455, 0.7875612212027712, 0.7806858036083019, 0.7772393373672368, 0.7711328857494851, 0.7709656992084097, 0.767799531571405, 0.7634265674698651], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 22.69672623599763, 'batch_acquisition_elapsed_time': 42.71371865800029})
store['iterations'].append({'num_epochs': 11, 'test_metrics': {'accuracy': 0.9433, 'nll': 0.5239746655124424}, 'chosen_samples': [54950, 165622, 51856, 171856, 41832, 48524, 161572, 174950, 45622, 101832], 'chosen_samples_score': [0.7916085517253655, 0.7866258007455976, 0.7834817971760968, 0.7798160933802103, 0.7788097819877324, 0.7772787049368091, 0.7766155652450539, 0.7738709693579984, 0.7719673733582234, 0.7709381605393725], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 22.455888829994365, 'batch_acquisition_elapsed_time': 39.32041984699754})