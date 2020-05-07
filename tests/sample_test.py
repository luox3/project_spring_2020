from nobel_winners.mini_nobel import get_data, find_winners
from pathlib import Path


tests_dir = Path(__file__).parent
tests_data_dir = tests_dir / 'data'
SAMPLE_CSV = tests_data_dir / 'raw_nobel.csv'

def test_get_data():

    expected = pd.DataFrame.read_csv(SAMPLE_CSV.with_name("sample_output.csv"))
    filename = SAMPLE_CSV
    result = get_data(filename)
    assert result == expected

def test_make_plots():
    expected = ['einstein','bohr']
    input_df = get_data(SAMPLE_CSV)
    make_plots(input_df)


def test_nothing_in_particular():
    from pathlib import Path
    current_dir = Path.cwd()
    print('hello world!')

    assert 2 + 2 != 5

def test_that_broken_means_broken():
    assert 4 == 2