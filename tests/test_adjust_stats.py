import pytest
import adjust_results4_isadog
import calculates_results_stats


def test_adjust_results4_isadog(tmp_path):
    results_dic = {
        'img1.jpg': ['golden retriever', 'golden retriever', 1],
        'img2.jpg': ['german shepherd', 'dalmatian', 0],
        'img3.jpg': ['tabby', 'siamese cat', 0],
        'img4.jpg': ['beagle', 'beagle', 1],
        'img5.jpg': ['persian cat', 'beagle', 0],
    }

    dogfile = tmp_path / 'dogs.txt'
    dogfile.write_text('\n'.join([
        'golden retriever',
        'german shepherd',
        'beagle',
        'dalmatian',
    ]))

    adjust_results4_isadog.adjust_results4_isadog(results_dic, str(dogfile))

    assert results_dic['img1.jpg'][3:] == [1, 1]
    assert results_dic['img2.jpg'][3:] == [1, 1]
    assert results_dic['img3.jpg'][3:] == [0, 0]
    assert results_dic['img4.jpg'][3:] == [1, 1]
    assert results_dic['img5.jpg'][3:] == [0, 1]
    assert all(len(v) == 5 for v in results_dic.values())


def test_calculates_results_stats():
    results_dic = {
        'image1.jpg': ['beagle', 'beagle', 1, 1, 1],
        'image2.jpg': ['german shepherd', 'dalmatian', 0, 1, 1],
        'image3.jpg': ['tabby', 'tabby', 1, 0, 0],
        'image4.jpg': ['cat', 'beagle', 0, 0, 1],
    }

    stats = calculates_results_stats.calculates_results_stats(results_dic)

    assert stats['n_images'] == 4
    assert stats['n_dogs_img'] == 2
    assert stats['n_notdogs_img'] == 2
    assert stats['n_match'] == 2
    assert stats['n_correct_dogs'] == 2
    assert stats['n_correct_notdogs'] == 1
    assert stats['n_correct_breed'] == 1

    assert stats['pct_match'] == pytest.approx(50.0)
    assert stats['pct_correct_dogs'] == pytest.approx(100.0)
    assert stats['pct_correct_breed'] == pytest.approx(50.0)
    assert stats['pct_correct_notdogs'] == pytest.approx(50.0)
