from git import Repo
from pydriller import RepositoryMining, GitRepository
from pydriller.domain.commit import ModificationType
from pprint import pprint

gr = GitRepository("demo")

for commit in RepositoryMining("demo").traverse_commits():
    for modified_file in commit.modifications:
        print(commit.hash + " modified file " + modified_file.filename)

# for commit in RepositoryMining("myrepo").traverse_commits():
#     print(commit.hash)
#     print(commit.msg)
#
# for commit in RepositoryMining("myrepo").traverse_commits():
#     for modified_file in commit.modifications:
#         print(modified_file.filename)
#
#         diff = modified_file.diff
#
#         parsed_diff = gr.parsed_diff(diff)
#         pprint(parsed_diff)