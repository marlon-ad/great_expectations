import unittest
import json
import hashlib
import datetime
import numpy as np
import pandas as pd

import great_expectations as ge


class TestDistributionalExpectations(unittest.TestCase):

    D = ge.df(pd.DataFrame({
        'norm_0_1' : [1.86466312629,0.598163544099,-0.686314834204,0.309810770507,0.535493433837,0.163388690372,0.533467038791,-0.452458199477,0.6128042924,-0.715518309472,0.664479673133,-0.772286247287,0.511436045264,0.34633454418,-0.0120123083816,0.80128761377,-0.58090988221,1.86359507146,0.27790976294,-0.598889926335,0.970343670716,-0.935420463358,0.587408513979,2.44082854938,0.0640571988566,-0.270837720219,2.21750329449,-2.1227831462,-0.0849270203954,1.77350545171,0.0454059511527,0.445408415592,-0.645070358507,-0.0466988453487,0.17084825884,-0.863431330633,1.20048807471,2.93308570168,-1.44365949831,0.303071032935,-2.257130212,0.961392676549,-1.05785027324,-0.0667377394975,1.1756023638,-0.884354420199,-0.801116773263,-1.33853837383,-0.798936151909,-1.73055262605,-0.432665548456,-0.284001361107,0.0316282125382,0.652663447169,-1.31557048835,-1.67733409538,-0.61256916892,0.493392559731,-0.802397345586,0.327369399957,0.322043536354,-0.664144332536,-0.415760602992,0.246630359218,-0.311962458627,-0.862671123374,-1.69452491381,-0.857326968618,0.108412082394,-1.09221731045,-0.568866461897,0.0781404238368,-1.23729933975,0.206139556935,-0.785468954657,-1.32025788316,-0.499964240017,0.973935377567,-0.134330562874,2.54552750423,2.03286081688,-0.111180501821,1.30302344022,-0.693186665311,0.437228753768,3.39283116651,3.204047169,-0.197115713505,0.0373215602847,-0.697221361091,0.11491291582,1.43424066427,1.67880904676,0.485618802167,-1.05137961439,-1.05820018686,0.47852904757,-1.45340403056,0.600652452415,-1.04030494199],
        'norm_1_1' :  [1.44324420023,0.318703328817,0.326659323018,-0.00853083988706,-0.131200924224,-0.95815934865,0.8671359644,0.678716257181,1.73998241325,0.922484823795,2.46837082143,1.87472003758,1.76922760927,2.49011390834,-0.25067936756,2.19127135191,1.27798098691,0.204024154836,0.746058633028,-0.0842233385703,1.7805746489,0.214567735825,2.06080869581,1.0058922947,0.923970034261,0.249592329632,2.31795445247,2.2727513623,1.45593832992,0.792260141447,-0.325052005608,-1.11535526114,1.09422143866,1.19702987848,1.45764688003,-0.168722282751,1.6023119983,1.13957052946,0.474104549922,-0.156615555875,3.05623438296,1.28393242696,1.90259696828,2.50200777406,1.52742799171,1.16965302399,-1.25479093468,1.00706349302,-0.250746586653,2.62272778582,1.21792956159,1.59565143521,0.619706299778,1.10152082786,2.56010645341,1.0752338423,0.434729254654,2.17822951433,0.397421122663,0.837208524156,1.37093347392,1.40550424013,1.80905560291,0.145666312777,0.581607338871,0.455645589281,0.203186995041,1.22214590342,2.00306925364,1.33978993846,1.17329696762,1.70627692637,0.521119268555,-0.20595865175,-0.229023040641,1.7279013096,-0.276146064303,0.216483189561,0.472667305604,1.45401995249,0.41045882653,0.952315314732,1.04162842785,1.43471685118,1.98475438278,0.085079569321,-0.404021557218,1.20002328453,1.26706265595,-0.29990472325,1.57787709361,0.509401116218,1.27848180567,-1.21622036979,0.229887819635,2.05072155713,0.238678031515,1.5739707112,2.45453289428,-0.306923527104],
        'bimodal' : [1.86466312629,0.598163544099,-0.686314834204,0.309810770507,0.535493433837,0.163388690372,0.533467038791,-0.452458199477,0.6128042924,-0.715518309472,0.664479673133,-0.772286247287,0.511436045264,0.34633454418,-0.0120123083816,0.80128761377,-0.58090988221,1.86359507146,0.27790976294,-0.598889926335,0.970343670716,-0.935420463358,0.587408513979,2.44082854938,0.0640571988566,-0.270837720219,2.21750329449,-2.1227831462,-0.0849270203954,1.77350545171,0.0454059511527,0.445408415592,-0.645070358507,-0.0466988453487,0.17084825884,-0.863431330633,1.20048807471,2.93308570168,-1.44365949831,0.303071032935,-2.257130212,0.961392676549,-1.05785027324,-0.0667377394975,1.1756023638,-0.884354420199,-0.801116773263,-1.33853837383,-0.798936151909,-1.73055262605,9.5222778176,11.146417443,9.45136336205,7.4307518559,8.75219811571,10.3823936054,9.29852974249,9.15062691637,10.218136547,10.1593749219,10.9478414773,10.8222547348,10.9109809664,9.80637003158,10.3512708363,9.7641908085,12.4560168885,9.85159850706,9.0510039736,8.98913974317,10.2162875826,10.7151772009,10.6454321399,9.30520007605,11.2343561935,9.69456264261,10.1282854751,11.072488419,10.5344858288,8.71418259804,10.7544541913,8.00696908999,12.0336736381,10.3941841473,9.31572623073,9.71341207949,10.9358397156,8.69433737287,10.1700213822,9.5851372466,10.382155099,8.46211016028,9.17304384738,10.7920030101,9.51702067279,9.45003153565,9.97686637259,10.2814734223,10.3401131141,10.2822279477],
        'categorical_fixed': ['A', 'B', 'B', 'B', 'C', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'C',  'A', 'A', 'C', 'A', 'A', 'A', 'A', 'A', 'C', 'B', 'A', 'A', 'A',  'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B',  'A', 'C', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'C',  'A', 'A', 'C', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'C',  'A', 'B', 'A', 'C', 'A', 'A', 'B', 'C', 'B', 'A', 'A', 'A', 'A',  'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'C', 'B', 'B', 'B',  'C', 'C', 'B', 'B', 'B', 'A', 'B', 'C', 'B']
    }))

    auto_partition_norm_0_1 = {
        'partition': [ -2.25713021e+00,  -1.69213407e+00,  -1.12713794e+00, -5.62141798e-01,   2.85433940e-03,   5.67850477e-01, 1.13284662e+00,   1.69784275e+00,   2.26283889e+00, 2.82783503e+00,   3.39283117e+00],
        'weights': [ 0.04,  0.07,  0.25,  0.14,  0.25,  0.1 ,  0.05,  0.05,  0.02,  0.03]
        }

    uniform_partition_norm_0_1 = {
        'partition': [ -2.25713021e+00,  -1.69213407e+00,  -1.12713794e+00,-5.62141798e-01,   2.85433940e-03,   5.67850477e-01, 1.13284662e+00,   1.69784275e+00,   2.26283889e+00,2.82783503e+00,   3.39283117e+00],
        'weights': [ 0.04,  0.07,  0.25,  0.14,  0.25,  0.1 ,  0.05,  0.05,  0.02,  0.03]
    }

    ntile_partition_norm_0_1 = {
        'partition': [-2.25713021, -1.24512645, -0.8583958 , -0.67079548, -0.35348172, 0.00980795,  0.22233588,  0.48065597,  0.65502669,  1.68827869, 3.39283117],
        'weights': [ 0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1]
    }

    kde_smooth_partition_norm_0_1 = {
        'partition': [-2.854290967829737,   -2.4561837972762395,   -2.0241789009147495,   -1.5921740045532593,   -1.160169108191769,   -0.7281642118302791,   -0.29615931546878915,   0.13584558089270127,   0.5678504772541912,   0.9998553736156812,   1.4318602699771712,   1.8638651663386612,   2.295870062700151,   2.727874959061642,   3.159879855423132,   3.5918847517846224,   3.9899919223381195],
        'weights': [0.0075436804103899743,   0.018019194359718937,   0.041259328964376174,   0.08053792035119961,   0.12362991210905325,   0.14567952814630236,   0.15225597079545095,   0.14327947097169935,   0.1032870530285479,   0.0601158228190406,   0.0390362149165715,   0.029877889371157096,   0.022063433271194755,   0.01625697417105365,   0.011026357073663506,   0.0061312492405803942]
    }

    auto_partition_bimodal = {
        'partition': [ -2.25713021,  -0.41798682,   1.42115656,   3.26029995,   5.09944334,   6.93858673,   8.77773011,  10.6168735 ,  12.45601689],
        'weights': [ 0.18,  0.26,  0.06,  0.  ,  0.  ,  0.06,  0.31,  0.13]
    }

    kde_smooth_partition_bimodal = {
        'partition': [-2.854290967829737,   -2.4561837972762395,   -2.0364267341910796,   -1.6166696711059196,   -1.1969126080207597,   -0.7771555449355998,   -0.3573984818504399,   0.062358581234720045,   0.48211564431987997,   0.9018727074050399,   1.3216297704901998,   1.7413868335753597,   2.1611438966605196,   2.5809009597456796,   3.0006580228308395,   3.4204150859159994,   3.8401721490011593,   4.25992921208632,   4.679686275171479,   5.0994433382566395,   5.519200401341799,   5.938957464426959,   6.35871452751212,   6.778471590597279,   7.198228653682438,   7.617985716767599,   8.03774277985276,   8.457499842937919,   8.877256906023078,   9.297013969108239,   9.7167710321934,   10.136528095278559,   10.556285158363718,   10.976042221448878,   11.39579928453404,   11.815556347619198,   12.235313410704357,   12.655070473789518,   13.053177644343014],
        'weights': [0.066368003332104852,   0.021818852934014005,   0.02584083959663694,   0.029578001957852706,   0.0327242515369664,   0.03500023161366317,   0.036194963953556814,   0.036198899121276884,   0.03502116492186086,   0.03278736952129502,   0.029718947127573725,   0.02609932397920761,   0.022234851231160424,   0.018418812389548123,   0.01490497267951818,   0.011893869455697703,   0.009531427749437715,   0.007916510836748492,   0.007112306971326199,   0.007156208299303357,   0.00806392333575856,   0.009825656773428615,   0.01239486441773796,   0.01567283100322614,   0.01949450782499751,   0.02362202163487037,   0.027751485424536426,   0.03153604218636141,   0.034623887594422365,   0.03670540996238303,   0.03756000271832394,   0.0370918867667156,   0.03534610963363327,   0.03250042840942269,   0.028834710974702804,   0.02468494915380226,   0.02039227746465966,   0.057379195512268222]
    }

    categorical_partition = {
        'partition': ['A', 'B', 'C'],
        'weights': [ 0.54,  0.32,  0.14]
    }

    categorical_partition_alternate = {
        'partition': ['A', 'B', 'C'],
        'weights': [ 0.33333333,  0.33333333,  0.33333333]
    }

    def test_expect_column_chisquare_test_p_value_greater_than(self):
        T = [
                {
                    'args': ['categorical_fixed'],
                    'kwargs': {
                        'partition_object': self.categorical_partition,
                        'p': 0.05
                        },
                    'out': {'success': True, 'true_value': 1.}
                },
                {
                    'args': ['categorical_fixed'],
                    'kwargs': {
                        'partition_object': self.categorical_partition_alternate,
                        'p': 0.05
                    },
                    'out': {'success': False, 'true_value': 5.9032936302303462e-06}
                }
        ]
        for t in T:
            out = self.D.expect_column_chisquare_test_p_value_greater_than(*t['args'], **t['kwargs'])
            self.assertEqual(out['success'],t['out']['success'])
            self.assertEqual(out['true_value'], t['out']['true_value'])
            #out = self.D.expect_column_frequency_distribution_to_be(*t['args'], **t['kwargs'])
            #self.assertTrue(np.allclose(out['success'], t['out']['success']))
            #self.assertTrue(np.allclose(out['true_value'], t['out']['true_value']))

    def test_expect_column_kl_divergence_to_be_discrete(self):
        T = [
                {
                    'args': ['categorical_fixed'],
                    'kwargs': {
                        'partition_object': self.categorical_partition,
                        'threshold': 0.1
                        },
                    'out': {'success': True, 'true_value': 0.}
                },
                {
                    'args': ['categorical_fixed'],
                    'kwargs': {
                        'partition_object': self.categorical_partition_alternate,
                        'threshold': 0.1
                        },
                    'out': {'success': False, 'true_value': 0.12599700286677529}
                }
        ]
        for t in T:
            out = self.D.expect_column_kl_divergence_to_be(*t['args'], **t['kwargs'])
            self.assertTrue(np.allclose(out['success'], t['out']['success']))
            self.assertTrue(np.allclose(out['true_value'], t['out']['true_value']))

    def test_expect_column_bootrapped_ks_test_p_value_greater_than(self):
        T = [
                {
                    'args': ['norm_0_1'],
                    'kwargs':{'partition_object': self.auto_partition_norm_0_1, "p": 0.05},
                    'out':{'success':True, 'true_value': "RANDOMIZED"}
                },
                {
                    'args': ['norm_0_1'],
                    'kwargs':{'partition_object': self.uniform_partition_norm_0_1, "p": 0.05},
                    'out':{'success':True, 'true_value': "RANDOMIZED"}
                },
                {
                    'args': ['norm_0_1'],
                    'kwargs':{'partition_object': self.ntile_partition_norm_0_1, "p": 0.05},
                    'out':{'success':True, 'true_value': "RANDOMIZED"}
                },
                {
                    'args': ['norm_0_1'],
                    'kwargs':{'partition_object': self.kde_smooth_partition_norm_0_1, "p": 0.05},
                    'out':{'success':True, 'true_value': "RANDOMIZED"}
                },
                {
                    'args': ['norm_1_1'],
                    'kwargs':{'partition_object': self.auto_partition_norm_0_1, "p": 0.05},
                    'out':{'success':False, 'true_value': "RANDOMIZED"}
                },
                {
                    'args': ['norm_1_1'],
                    'kwargs':{'partition_object': self.uniform_partition_norm_0_1, "p": 0.05},
                    'out':{'success':False, 'true_value': "RANDOMIZED"}
                },
                {
                    'args': ['norm_1_1'],
                    'kwargs':{'partition_object': self.ntile_partition_norm_0_1, "p": 0.05},
                    'out':{'success':False, 'true_value': "RANDOMIZED"}
                },
                {
                    'args': ['norm_1_1'],
                    'kwargs':{'partition_object': self.kde_smooth_partition_norm_0_1, "p": 0.05},
                    'out':{'success':False, 'true_value': "RANDOMIZED"}
                },
                {
                    'args': ['bimodal'],
                    'kwargs':{'partition_object': self.auto_partition_bimodal, "p": 0.05},
                    'out':{'success':True, 'true_value': "RANDOMIZED"}
                },
                {
                    'args': ['bimodal'],
                    'kwargs':{'partition_object': self.kde_smooth_partition_bimodal, "p": 0.05},
                    'out':{'success':True, 'true_value': "RANDOMIZED"}
                },
                {
                    'args': ['bimodal'],
                    'kwargs':{'partition_object': self.auto_partition_norm_0_1, "p": 0.05},
                    'out':{'success':False, 'true_value': "RANDOMIZED"}
                },
                {
                    'args': ['bimodal'],
                    'kwargs':{'partition_object': self.uniform_partition_norm_0_1, "p": 0.05},
                    'out':{'success':False, 'true_value': "RANDOMIZED"}
                }
            ]
        #trials = 30
        for t in T:
            # Evaluate the expectation a given number of times
            #results = [ self.D.expect_column_numerical_distribution_to_be(*t['args'], **t['kwargs'])['success'] for x in range(trials) ]
            # Assert that there are fewer incorrect results than twice p value
            #self.assertLess(results.count(not t['out']['success']) / trials, 2. * t['kwargs']['p'])
            out = self.D.expect_column_bootstrapped_ks_test_p_value_greater_than(*t['args'], **t['kwargs'])
            self.assertEqual(out['success'], t['out']['success'])

    def test_expect_column_kl_divergence_to_be_continuous(self):
        T = [
# {'true_value': 0.0013326972943566281, 'success': True}
# {'true_value': 0.0013326972943566281, 'success': True}
# {'true_value': 0.00047210715733547086, 'success': True}
# {'true_value': 0.039351496030977519, 'success': True}
# {'true_value': 0.56801971244750626, 'success': False}
# {'true_value': 0.56801971244750626, 'success': False}
# {'true_value': 0.59398892510202805, 'success': False}
# {'true_value': 0.52740442919069253, 'success': False}
# {'true_value': 0.00023525468906568868, 'success': True}
# {'true_value': 0.53180538113092268, 'success': False}
# {'true_value': 0.027543614241485374, 'success': True}
# {'true_value': 0.027543614241485374, 'success': True}
                {
                    'args': ['norm_0_1'],
                    'kwargs':{"partition_object": self.auto_partition_norm_0_1, "threshold": 0.1},
                    'out':{'success':True, 'true_value': 0.0013326972943566281}
                },
                {
                    'args': ['norm_0_1'],
                    'kwargs':{"partition_object": self.uniform_partition_norm_0_1, "threshold": 0.1},
                    'out':{'success':True, 'true_value': 0.0013326972943566281}
                },
                {
                    'args': ['norm_0_1'],
                    'kwargs':{"partition_object": self.ntile_partition_norm_0_1, "threshold": 0.1},
                    'out':{'success':True, 'true_value': 0.00047210715733547086}
                },
                {
                    'args': ['norm_0_1'],
                    'kwargs':{"partition_object": self.kde_smooth_partition_norm_0_1, "threshold": 0.1},
                    'out':{'success':True, 'true_value': 0.039351496030977519}
                },
                {
                    'args': ['norm_1_1'],
                    'kwargs':{"partition_object": self.auto_partition_norm_0_1, "threshold": 0.1},
                    'out':{'success':False, 'true_value': 0.56801971244750626}
                },
                {
                    'args': ['norm_1_1'],
                    'kwargs':{"partition_object": self.uniform_partition_norm_0_1, "threshold": 0.1},
                    'out':{'success':False, 'true_value': 0.56801971244750626}
                },
                {
                    'args': ['norm_1_1'],
                    'kwargs':{"partition_object": self.ntile_partition_norm_0_1, "threshold": 0.1},
                    'out':{'success':False, 'true_value': 0.59398892510202805}
                },
                {
                    'args': ['norm_1_1'],
                    'kwargs':{"partition_object": self.kde_smooth_partition_norm_0_1, "threshold": 0.1},
                    'out':{'success':False, 'true_value': 0.52740442919069253}
                },
                {
                    'args': ['bimodal'],
                    'kwargs':{"partition_object": self.auto_partition_bimodal, "threshold": 0.1},
                    'out':{'success':True, 'true_value': 0.00023525468906568868}
                },
                # TODO: Consider changes that would allow us to detect this case
                # },
                # {
                #     'args': ['bimodal', self.kde_smooth_partition_bimodal],
                #     'kwargs':{"threshold": 0.1},
                #     'out':{'success':True, 'true_value': "NOTTESTED"}
                # }
                # {
                #     'args': ['bimodal', self.auto_partition_norm_0_1],
                #     'kwargs':{"threshold": 0.1},
                #     'out':{'success':False, 'true_value': "NOTTESTED"}
                # },
                # {
                #     'args': ['bimodal', self.uniform_partition_norm_0_1],
                #     'kwargs':{"threshold": 0.1},
                #     'out':{'success':False, 'true_value': "NOTTESTED"}
                # }
        ]
        for t in T:
            out = self.D.expect_column_kl_divergence_to_be(*t['args'], **t['kwargs'])
            self.assertTrue(np.allclose(out['success'],t['out']['success']))

if __name__ == "__main__":
    unittest.main()
