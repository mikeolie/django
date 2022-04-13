#!/bin/sh
branch_name=$(git branch | sed -n -e 's/^\* \(.*\)/\1/p')

echo "Staging to git..."

git add .

read -r -p "Commit Message: " commit_msg 

git commit -m "${commit_msg}"

git push origin $branch_name

echo "Success!"    