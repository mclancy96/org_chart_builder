import json


def select_ids_for_tree(manager_id, json_file):
    title_id_tree_list = [manager_id]
    titles = []
    with open(json_file) as f:
        titles = json.load(f)
    recursive_id_lookup(manager_id, titles, title_id_tree_list)
    return title_id_tree_list


def recursive_id_lookup(manager_id, titles, title_id_tree_list):
    managed_titles_list = managed_titles(titles, manager_id)
    # Base case
    if managed_titles_list == []:
        if manager_id not in title_id_tree_list:
            title_id_tree_list.append(manager_id)
        return
    # Recursive
    for title in managed_titles_list:
        if title not in title_id_tree_list:
            title_id_tree_list.append(title)
        recursive_id_lookup(title, titles, title_id_tree_list)


def managed_titles(title_list, manager_id):
    return [x["id"]
            for x in title_list
            if x["managed_by_title_id"] == manager_id]
