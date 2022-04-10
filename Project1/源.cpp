#include <cstdio>
#include <cmath>
#include <fstream>
using namespace std;


int main() {
	ofstream out95("95.txt", ios::out);
	ofstream out90("90.txt", ios::out);
	for (int T = 1; T < 10000; T++) {
		int K95 = T - (int)ceil(0.95 * T);
		out95 << K95 << "\n";
		int K90 = T - (int)ceil(0.9 * T);
		out90 << K90 << "\n";
	}
}