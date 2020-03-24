num = 0;
for (num = 0; i < N; i++) 
    for (num = 0; j < i; j++) 
        count++;
print(num)
########################
int count = 0;
for (int i = N; i > 0; i /= 2) 
    for (int j = 0; j < i; j++) 
        count++;
#########################
for (int i = 1; i < n; i = i * 2){
    console.log("Hey - I'm busy looking at: " + i);
}
########################
for (int i = 1; i <= n; i++){
    for(int j = 1; j < 8; j = j * 2) {
        console.log("Hey - I'm busy looking at: " + i + " and " + j);
    }
}
#######################
for (int i = 1; i <= Math.pow(2, n); i++){
   console.log("Hey - I'm busy looking at: " + i);
}