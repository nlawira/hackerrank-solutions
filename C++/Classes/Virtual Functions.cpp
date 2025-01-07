#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Person {
  public:
    string name;
    int age;
    virtual void putdata() = 0;
    virtual void getdata() = 0;
};

class Professor : public Person {
  public:
    int publications, cur_id;
    static int id;
    Professor() {
        cur_id = ++id;
    };
    void putdata() {
        cout << name << " " << age << " " << publications << " " << cur_id << endl;
    }
    void getdata() {
        string iname;
        int iage, ipublication;
        cin >> iname >> iage >> ipublication;
        name = iname;
        age = iage;
        publications = ipublication;
    }
};

class Student : public Person {
  public:
    int marks[6], cur_id;
    static int id;
    Student() {
        cur_id = ++id;
    }
    void putdata() {
        int total = 0;
        for (int i=0; i<6; i++){
            total += marks[i];
        }
    cout << name << " " << age << " " << total << " " << cur_id << endl;
    }
    void getdata() {
        string iname;
        int iage;
        cin >> iname >> iage;
        for (int i=0; i<6; i++) {
            int temp;
            cin >> temp;
            marks[i] = temp;
        }
        name = iname;
        age = iage;
    }
};

int Student::id = 0;
int Professor::id = 0;

int main(){

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}
