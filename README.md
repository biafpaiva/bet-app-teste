# The App
## **1. Description**
World Cup BetApp project for software engineer class (dcc072), a web application made with NEXTJS and FLASK. This program supports two kinds of users: gamblers and one  administrator. In general, gamblers can make bets and compare score with other users in a rank. The administrator is responsible for the registration of the match real results. There also are other features like delete bets and change username. 

<br/>
<h3 align="center">Gamblers</h3>
<br/>

<p align="center">
<img src="https://sat02pap005files.storage.live.com/y4m2ucS1iXi1L0FC_2Gjw09MEq-R7dBvEZcyL2ZaNYImpm95BglCOGmUeaRAtE8gYMZDA7Ej0VscgOJ-4MAgB8ODCwl9hejCMvh45JKDxTftPLkEJNBfxS1J2_pzKFtdN4_zN9JLUhGbPWNU_VSnUxQUYrooUrr9fcdRenpFpMcne0yzBq5j8xKyzGmZr3v0XZ_kZmzWYzWA9udfkSS-mA29OJv5zqB0OxNtqwcOHQ0mEw?encodeFailures=1&width=407&height=880" height="600" >
  
<img src="https://sat02pap005files.storage.live.com/y4mi9KYp-zXBjdwa_REhh9VOQMSG1pdi7v2m7e9u1AklqmODxuS9ttBCNF00J0zTzGKn2oldH63tplqnS-HsbqWpLH82FbKokJ_kosDmHc74hKcpdKo9MSadAfhjQE6zuXWwMZf8czed8KTAkveHEJ6CQSPtjgcTs6S6XzAbeEPD7lq93cO7sCU61D0QdXgW1c5UA3c1-Zt8pQt6vp9tt44Dr1quaBrYKMe9pUhMy3S0Ow?encodeFailures=1&width=407&height=880" height="600" hspace="20">  

<img src="https://sat02pap005files.storage.live.com/y4mG5bcwjKZO8VJCYkmYRoq-DXrC8omk_3M0GrDiNs6nMTTKDX68nHRbm339lTzx4_DsktzVBySg2BfHd3m0ZDjYeKd5vUoa-yYN1jBqkjViCkcJfpsImIz-f-pV6Z7uWkIXbYRTkhNCvdskLfc-1Giq6CnPEJdHYkooM_9WeOND6D4fjwXZlEmQsDD3485z7WhfKGpnkoj8ycsydQllZxOnh3Kaosqw4G8viu643xyhI0?encodeFailures=1&width=407&height=880" height="600" hspace="20">
</p>


<br/>
<h3 align="center">Administrator</h3>
<br/>

<p align="center">
<img src="https://sat02pap005files.storage.live.com/y4mLVnskL3igzdOJKMO6g5NtvEpMOEwl85ECwBQpUd0Zymj1uueoqnbn8_SHQlNR8Y1n2MaDmm9ieGoc03D7mL235OP5a2UxROdhxQB2qeB66s4hBzvwS62dkWhClj4OGdfccTJAStdd4YDiMO6Yz8SCdP0T0QfGhJSd0LC3seU1mWah8ksxwmar2Rjzy1XEoKeXjOc6YIus-Q3GoWdKDIcdBYaKiWD_MrDZX3bCLAxBUw?encodeFailures=1&width=380&height=824" height="500">
  
<img src="https://sat02pap005files.storage.live.com/y4mqf8gwtgT_dsTCoAYtYeBh20MD98QWdWN-BGyPhU3ABFlbNxBwuR2Sqvn6qiNjV6405h2LkHQRgyhGkU8b3MAK6v4s73MKsoFgZncr99w94M840sGajk64tLF5220z10XgQRv8PjR_OannjlbcPmk-eRzf4F-g9j7_UL39kfbGQSVX2jMePczCD1F2gGNZNO5_cA4LA9-d8sY0iE0hi6aI6-Enc81zEVg4J-sNwjsQTU?encodeFailures=1&width=407&height=880" height="500" hspace="10">
  
<img src="https://sat02pap005files.storage.live.com/y4m56_HgqoMywrOsW_BSP7k6O-i7r44YAnh3VtnDL16T4v9dVHqSSYPIZGRuvUy9bzUgT0Nv4PQvKSigrOOT8EUpBMjz-s5uj2JqfCLKUNtcF2cZ6h5euOooUyKAhTkryp0-7z-GpgJHo5L_XydV7jiboKvpTNuIodq6rMTOY7gQhrIujrTmCAP1phgQtIU6TCWffNZNnNSCTrvYZaqkSorwzEk_ZSJEJItblAPbtgUF7I?encodeFailures=1&width=407&height=880" height="500" hspace="10">  
  
<img src="https://sat02pap005files.storage.live.com/y4mZHPl4KfZXjenvzKODSB9XftgfIGLk5z3gGWn2y3cTpn55_ruyJljhXKQHDQXq3_h-5o0vVRtg3g7LpnMd0NcGPlg5uO-qTjOB-Fq1U6668ZquCeJ6r2ITlrIj3zUyDBtB0GvOPcw4Ilf2gk2DB0PUyjVW53VaHl9ZTIyjlDKl0l-edaKgLyad-KuKVqU0GLzEcEXDwWjSTcIgQhZSiDmG44ZQ57tDykhu4ANBcaAjw8?encodeFailures=1&width=380&height=824" height="500" hspace="10">  
</p>

<br/>

## **2. How to run**

### **Environment setup**
You'll need some packages in your machine to be able to run this project. You can install using the commands below:

```bash
sudo apt install python3.10-venv
sudo apt install nodejs
sudo apt install npm
npm install --global yarn
```

### **1° Step: Running the server (backend)**
Open your terminal and switch to the project directory. Then, inside flask-backend folder, run the following commands:

```bash
python3 -m venv venv
source venv/bin/activate
pip install Flask
```

This is going to download all the files required by Flask to run the project locally.

Now, to start the server all you need is:
```bash
python3 app.py
```
### **2° Step: Running the client (frontend)**

In another terminal, open the next-frontend folder. Install all the node packages using: 

```bash
yarn
```

And finally, to run the frontend use:
```bash
yarn dev
```
That's it! Let's gooo 
