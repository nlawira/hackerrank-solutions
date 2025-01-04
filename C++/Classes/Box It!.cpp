#include<bits/stdc++.h>

using namespace std;
//Implement the class Box  
//l,b,h are integers representing the dimensions of the box

// The class should have the following functions : 
class Box {
private:
    int l_ = 0;
    int b_ = 0;
    int h_ = 0;
public:
// Constructors: 
    Box() {};
    Box(int l ,int b ,int h) : l_(l), b_(b), h_(h) {};
    Box(Box& B) : l_(B.getLength()), b_(B.getBreadth()), h_(B.getHeight()) {};

    int getLength(){ return l_; }; // Return box's length
    int getBreadth() { return b_; }; // Return box's breadth
    int getHeight() { return h_; };  //Return box's height
    long long CalculateVolume() {
        return (long long)l_*b_*h_;
    }; // Return the volume of the box

//Overload operator < as specified
    bool operator<(Box& b) {
        if (l_ < b.getLength()) {
            return true;
        }
        else if (l_ == b.getLength() && b_ < b.getBreadth()) {
            return true;
        } else if (l_ == b.getLength() && b_ == b.getBreadth() && h_ < b.getHeight()) {
            return true;
        }
        else { return false; }
    }

//Overload operator << as specified
    friend ostream& operator<<(ostream& out, Box& B) {
        out << B.getLength() << " " << B.getBreadth() << " " << B.getHeight();
        return out;
    }
};


void check2()
{
	int n;
	cin>>n;
	Box temp;
	for(int i=0;i<n;i++)
	{
		int type;
		cin>>type;
		if(type ==1)
		{
			cout<<temp<<endl;
		}
		if(type == 2)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			temp=NewBox;
			cout<<temp<<endl;
		}
		if(type==3)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			if(NewBox<temp)
			{
				cout<<"Lesser\n";
			}
			else
			{
				cout<<"Greater\n";
			}
		}
		if(type==4)
		{
			cout<<temp.CalculateVolume()<<endl;
		}
		if(type==5)
		{
			Box NewBox(temp);
			cout<<NewBox<<endl;
		}

	}
}

int main()
{
	check2();
}