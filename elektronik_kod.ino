void setup()
{

  Serial.begin(9600);
}

void loop()
{
//motor1
  int surme_deg1;
  int yon1;
  surme_deg1=analogRead(A0);
  surme_deg1=map(surme_deg1,0,1023,0,255);
  yon1=random(0,2);
//motor2
  int surme_deg2;
  int yon2;
  surme_deg2=analogRead(A0);
  surme_deg2=map(surme_deg2,0,1023,0,255);
  yon2=random(0,2);
//motor3
  int surme_deg3;
  int yon3;
  surme_deg3=analogRead(A0);
  surme_deg3=map(surme_deg3,0,1023,0,255);
  yon3=random(0,2);
//motor4
int surme_deg4;
  int yon4;
  surme_deg4=analogRead(A0);
  surme_deg4=map(surme_deg4,0,1023,0,255);
  yon4=random(0,2);
  //son print
  Serial.print("S");
  Serial.print(yon1);
  if (surme_deg1<10){
    Serial.print("00");
    Serial.print(surme_deg1);}  
  else if (surme_deg1<100){
    Serial.print("0");
    Serial.print(surme_deg1);}
  else {
    Serial.print(surme_deg1);};
    Serial.print(yon2);
  if (surme_deg2<10){
    Serial.print("00");
    Serial.print(surme_deg2);}  
  else if (surme_deg2<100){
    Serial.print("0");
    Serial.print(surme_deg2);}
  else {
    Serial.print(surme_deg2);};
    Serial.print(yon3);
  if (surme_deg3<10){
    Serial.print("00");
    Serial.print(surme_deg3);}  
  else if (surme_deg3<100){
    Serial.print("0");
    Serial.print(surme_deg3);}
  else {
    Serial.print(surme_deg3);};
    Serial.print(yon4);
  if (surme_deg4<10){
    Serial.print("00");
    Serial.print(surme_deg1);}  
  else if (surme_deg4<100){
    Serial.print("0");
    Serial.print(surme_deg4);}
  else {
    Serial.print(surme_deg4);};
  Serial.println("F");
}
