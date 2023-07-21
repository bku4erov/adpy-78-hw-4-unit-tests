import pytest

from main import get_unique_ids, list_to_dict, queries_by_words_distr


class TestUniqueIds:
    @pytest.mark.parametrize(
        'ids,expected', [
            ({'user1': [213, 213, 213, 15, 213],
			'user2': [54, 54, 119, 119, 119],
			'user3': [213, 98, 98, 35]},
            [15, 35, 54, 98, 119, 213]),
            ({'user1': [213, 1, 5, 15, 7]},
            [1, 5, 7, 15, 213]),
            ({'user1': [213, 213, 213, 15, 213],
			'user2': [54, 54, 119, 119, 119],
			'user3': [35]},
            [15, 35, 54, 119, 213]),
        ]
    )
    def test_with_correct_dict(self, ids, expected):
        result = get_unique_ids(ids)
        assert result == expected

    @pytest.mark.xfail
    @pytest.mark.parametrize(
        'ids,expected', [
            ({'user1': [213, 213, 213, 15, 213],
			'user2': [54, 54, 119, 119, 119],
			'user3': [213, 98, 98, 35]},
            [15, 35, 54, 98, 119]),
            ({'user1': [213, 1, 5, 15, 7]},
            [1, 7, 5, 15, 213]),
            ({'user1': [213, 213, 213, 15, 213],
			'user2': [54, 54, 119, 119, 119],
			'user3': [35]},
            [15, 35, 54, 119, 98, 213]),
        ]
    )
    def test_with_wrong_data(self, ids, expected):
        result = get_unique_ids(ids)
        assert result == expected

    @pytest.mark.xfail
    @pytest.mark.parametrize(
        'ids,expected', [
            ([[213, 213, 213, 15, 213],
			[54, 54, 119, 119, 119],
			[213, 98, 98, 35]],
            None),
            ({'user1': [213, [1, 5, 15, 7]]},
            None),
            ('some text',
            None),
        ]
    )
    def test_with_no_dict(self, ids, expected):
        result = get_unique_ids(ids)
        assert result == expected