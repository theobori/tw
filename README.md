# 🥐 tw

A CLI to deploy server and play Teeworlds throught Docker.

## 📖 How to build and run ?

1. Install the dependencies 
   - `python` >= **3.11**
   - `docker`*

2. Install the CLI
```bash
sudo make install
```
3. Run `tw -h`

## 📜 usage example

```bash
tw server -l
tw server -k vanilla --build
tw server -k vanilla --run
tw server -k vanilla --run -p 8303 -c $PWD/autoexec.cfg

tw client --run teeworlds
```

⚠️ To run with a database, you must build with the flag

❌ `--with-sql` is currently disbaled

```bash
tw server -k ddnet --build --with-sql
tw server -k ddnet --run --with-sql
```

## ℹ️ Note

This CLI assumes that youre using X with an UNIX system based.

Every available `keys`

| Server | Client |
:--- | :---: |
| FNG2 | Teeworlds (default) |
| Vanilla | |
| DDNet | |

## ✍️ TODO

| Feature | State |
:--- | :---: |
Add a database | ❌
Add Docker volume for the storage | ❌
Fix package relative imports | ✅
Server custom config file | ✅
Build and install `tw` as a CLI command | ✅
Add a CLI arg to list the available keys | ✅
Mount volume client side for user dir | ✅
Forward UDP instead of TCP | ✅
