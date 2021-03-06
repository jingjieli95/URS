from urs.praw_scrapers import Subreddit
from urs.utils import Global

### Function names are pretty self-explanatory, so I will not be adding comments 
### above the functions.

### Includes a total of 49 tests.

class TestCheckSubredditsListSubredditsMethod():
    """
    Testing CheckSubreddits class list_subreddits() method found on line 40 in 
    Subreddit.py.
    Have to find a way to test functions that access Reddit without exposing my 
    personal credentials. Passing for now.
    """

    def test_list_subreddits_valid_subreddits(self):
        pass

    def test_list_subreddits_invalid_subreddits(self):
        pass

    def test_list_subreddits_no_subreddits_left_to_process(self):
        pass

class TestPrintConfirmPrintEachMethod():
    """
    Testing PrintConfirm class _print_each() method found on line 64 in Subreddit.py.
    Have to find a way to test functions that access Reddit without exposing my 
    personal credentials. Passing for now.
    """

    def test_print_each(self):
        pass

class TestPrintConfirmPrintSettingsMethod():
    """
    Testing PrintConfirm class print_settings() method found on line 78 in 
    Subreddit.py.
    Have to find a way to test functions that access Reddit without exposing my 
    personal credentials. Passing for now.
    """

    def test_print_settings(self):
        pass

class TestPrintConfirmConfirmSettingsMethod():
    """
    Testing PrintConfirm class confirm_settings() method found on line 95 in 
    Subreddit.py.
    Have to find a way to test functions that access Reddit without exposing my 
    personal credentials. Passing for now.
    """

    def test_confirm_settings_yes(self):
        pass

    def test_confirm_settings_no(self):
        pass

    def test_confirm_settings_invaid_option(self):
        pass

class TestGetRulesGetMethod():
    """
    Testing GetRules class get() method found on line 130 in Subreddit.py.
    """

    def test_get(self):
        pass

class TestGetPostsSwitchInitMethod():
    """
    Testing GetPostsSwitch class __init__() method found on line 116 in 
    Subreddit.py.
    Have to find a way to test functions that access Reddit without exposing my 
    personal credentials. Passing for now.
    """

    def test_get_posts_switch_init_method_hot_instance_variable(self):
        pass

    def test_get_posts_switch_init_method_new_instance_variable(self):
        pass

    def test_get_posts_switch_init_method_controversial_instance_variable(self):
        pass

    def test_get_posts_switch_init_method_top_instance_variable(self):
        pass

    def test_get_posts_switch_init_method_rising_instance_variable(self):
        pass

    def test_get_posts_switch_init_method_switch_instance_variable(self):
        pass

class TestGetPostsSwitchScrapeSubMethod():
    """
    Testing GetPostsSwitch class scrape_sub() method found on line 136 in 
    Subreddit.py.
    Have to find a way to test functions that access Reddit without exposing my 
    personal credentials. Passing for now.
    """

    def test_scrape_sub_hot_switch(self):
        pass

    def test_scrape_sub_new_switch(self):
        pass

    def test_scrape_sub_controversial_switch(self):
        pass

    def test_scrape_sub_top_switch(self):
        pass

    def test_scrape_sub_rising_switch(self):
        pass

class TestGetPostsCollectSearchMethod():
    """
    Testing GetPosts class _collect_search() method found on line 146 in 
    Subreddit.py.
    Have to find a way to test functions that access Reddit without exposing my 
    personal credentials. Passing for now.
    """

    def test_collect_search(self):
        pass

class TestGetPostsCollectOthersMethod():
    """
    Testing GetPosts class _collect_others() method found on line 159 in Subreddit.py.
    Have to find a way to test functions that access Reddit without exposing my 
    personal credentials. Passing for now.
    """

    def test_collect_others_subreddit_args(self):
        pass

    def test_collect_others_basic_arg(self):
        pass

class TestGetPostsGetMethod():
    """
    Testing GetPosts class get() method found on line 175 in Subreddit.py.
    Have to find a way to test functions that access Reddit without exposing my 
    personal credentials. Passing for now.
    """

    def test_get_search_category(self):
        pass

    def test_get_other_categories(self):
        pass

class TestSortPostsInitMethod():
    """
    Testing SortPosts class __init__() method found on line 188 in Subreddit.py.
    """

    def test_sort_posts_init_method_titles_instance_variable(self):
        assert Subreddit.SortPosts()._titles == \
            [
                "title", 
                "flair", 
                "date_created", 
                "upvotes", 
                "upvote_ratio", 
                "id", 
                "edited", 
                "is_locked", 
                "nsfw", 
                "is_spoiler", 
                "stickied", 
                "url", 
                "comment_count", 
                "text"
            ]

class TestSortPostsInitializeDictMethod():
    """
    Testing SortPosts class _initialize_dict() method found on line 207 in 
    Subreddit.py.
    """

    def test_initialize_dict_csv_args(self):
        # args = None
        # titles = ["Title", "Flair", "Date Created", "Upvotes", "Upvote Ratio", 
        #     "ID", "Edited?", "Is Locked?", "NSFW?", "Is Spoiler?", "Stickied?", 
        #     "URL", "Comment Count", "Text"]

        # assert Subreddit.SortPosts()._initialize_dict(args) == \
        #     Global.make_list_dict(titles)

        pass
    
    def test_initialize_dict_json_args(self):
        # args = None
        # assert Subreddit.SortPosts()._initialize_dict(args) == dict()

        pass

class TestSortPostsFixEditDateMethod():
    """
    Testing SortPosts class _fix_edit_date() method found on line 211 in 
    Subreddit.py.
    Have to find a way to test functions that access Reddit without exposing my 
    personal credentials. Passing for now.
    """

    def test_fix_edit_date_if_edited(self):
        pass

    def test_fix_edit_date_not_edited(self):
        pass

class TestSortPostsFixGetDataMethod():
    """
    Testing SortPosts class _get_data() method found on line 217 in Subreddit.py.
    Have to find a way to test functions that access Reddit without exposing my 
    personal credentials. Passing for now.
    """

    def test_get_data(self):
        pass

class TestSortPostsCsvFormatMethod():
    """
    Testing SortPosts class _csv_format() method found on line 238 in Subreddit.py.
    Have to find a way to test functions that access Reddit without exposing my 
    personal credentials. Passing for now.
    """

    def test_csv_format(self):
        pass

class TestSortPostsMakeJsonSkeletonMethod():
    """
    Testing SortPosts class _make_json_skeleton() method found on line 271 in 
    Subreddit.py.
    """

    def test_make_json_skeleton(self):
        test_skeleton = Subreddit.SortPosts()._make_json_skeleton("S", "test", "askreddit", "all")
        assert test_skeleton == {
            "scrape_settings": {
                "subreddit": "askreddit",
                "category": "search",
                "n_results_or_keywords": "test",
                "time_filter": "all"
            },
            "data": []
        }

class TestSortPostsAddJsonSubredditRulesMethod():
    """
    Testing SortPosts class _add_json_subreddit_rules() method found on line 285
    in Subreddit.py.
    Have to find a way to test functions that access Reddit without exposing my 
    personal credentials. Passing for now.
    """

    def _add_json_subreddit_rules(self):
        pass

class TestSortPostsAddJsonSubmissionDataMethod():
    """
    Testing SortPosts class _add_json_submission_data() method found on line 291
    in Subreddit.py.
    Have to find a way to test functions that access Reddit without exposing my 
    personal credentials. Passing for now.
    """

    def test_add_json_submission_data(self):
        pass

class TestSortPostsSortMethod():
    """
    Testing SortPosts class sort() method found on line 249 in Subreddit.py.
    Have to find a way to test functions that access Reddit without exposing my 
    personal credentials. Passing for now.
    """

    def test_sort_with_csv_args(self):
        pass

    def test_sort_without_csv_args(self):
        pass

class TestGetSortWriteGetSortMethod():
    """
    Testing GetSortWrite class _get_sort() method found on line 275 in Subreddit.py.
    Have to find a way to test functions that access Reddit without exposing my 
    personal credentials. Passing for now.
    """

    def test_get_sort(self):
        pass

class TestGetSortWriteDetermineExportMethod():
    """
    Testing GetSortWrite class _determine_export() method found on line 280 in 
    Subreddit.py.
    Have to find a way to test functions that access Reddit without exposing my 
    personal credentials. Passing for now.
    """

    def test_determine_export_with_csv_args(self):
        pass

    def test_determine_export_without_csv_args(self):
        pass

class TestGetSortWritePrintConfirmMethod():
    """
    Testing GetSortWrite class _print_confirm() method found on line 288 in 
    Subreddit.py.
    Have to find a way to test functions that access Reddit without exposing my 
    personal credentials. Passing for now.
    """

    def test_print_confirm_with_csv_args(self):
        pass

    def test_print_confirm_without_csv_args(self):
        pass

class TestGetSortWriteWriteMethod():
    """
    Testing GetSortWrite class _write() method found on line 299 in Subreddit.py.
    Have to find a way to test functions that access Reddit without exposing my 
    personal credentials. Passing for now.
    """

    def test_write(self):
        pass

class TestGetSortWriteGswMethod():
    """
    Testing GetSortWrite class gsw() method found on line 305 in Subreddit.py.
    Have to find a way to test functions that access Reddit without exposing my 
    personal credentials. Passing for now.
    """

    def test_gsw_with_basic_args(self):
        pass

    def test_gsw_with_cli_args(self):
        pass

class TestRunSubredditCreateSettingsMethod():
    """
    Testing RunSubreddit class _create_settings() method found on line 320 in 
    Subreddit.py.
    Have to find a way to test functions that access Reddit without exposing my 
    personal credentials. Passing for now.
    """

    def test_create_settings(self):
        pass

class TestRunSubredditConfirmWriteMethod():
    """
    Testing RunSubreddit class _confirm_write() method found on line 330 in 
    Subreddit.py.
    Have to find a way to test functions that access Reddit without exposing my 
    personal credentials. Passing for now.
    """

    def test_confirm_write_with_confirm_option(self):
        pass

    def test_confirm_write_with_deny_option(self):
        pass

class TestRunSubredditWriteFileMethod():
    """
    Testing RunSubreddit class _write_file() method found on line 343 in 
    Subreddit.py.
    Have to find a way to test functions that access Reddit without exposing my 
    personal credentials. Passing for now.
    """

    def test_write_file_with_y_arg(self):
        pass

    def test_write_file_without_y_arg(self):
        pass
