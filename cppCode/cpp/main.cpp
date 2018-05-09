#include <iostream>
#include <fstream>
#include <ctime>
using namespace std;


int main()
{

	std::clock_t start;
	double duration;
	std::ofstream myfile;
	int counter = 0;
	start = std::clock();
	
	while(counter < 100)
	{
		counter++;
		myfile.open("dataCPP.txt", std::ios_base::app);
		myfile << counter;
		myfile << "\n";
		myfile.close();
	}
	
	duration = ( std::clock() - start ) / (double) CLOCKS_PER_SEC;
	myfile.open("dataCPP.txt", std::ios_base::app);
	myfile << "\n";
	myfile << "Duration: ";
	myfile << duration;
	myfile << " seconds.";
	


}
