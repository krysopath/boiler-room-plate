rm -rf .git

git init
git add .
git commit -m "Initial commit"

git remote add origin git@github.com:krysopath/boiler-room-plate.git
git push -u --force origin master
