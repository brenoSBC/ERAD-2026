#include <iostream>
#include <vector>
#include <string>
#include <limits>
#include <cmath>
#include "dados.hpp"

using namespace std;

double media(const vector<double> &vetor) {

    double soma = 0.0;
    for(double elemento : vetor) {
        soma+=elemento;
    }

    return soma / vetor.size();
}

double media_geometrica(vector<double>& best_medias) {

     double log_sum = 0.0;

    for (double x : best_medias) {
        log_sum += log(x);
    }

    return exp(log_sum / best_medias.size());
}

void run(const string &name,
         const vector<vector<double>> &openmpi,
         const vector<vector<double>> &resipipe,
         vector<double> &best_media_omp,
         vector<double> &best_media_res) {

    cout << "Aplicação: " << name << "\n";

    double best_media_openmpi = numeric_limits<double>::lowest();
    int best_config_openmpi = -1;

    double best_media_resipipe = numeric_limits<double>::lowest();
    int best_config_resipipe = -1;

    for(int i = 0; i < 6; i++) {
        double media_openmpi = media(openmpi[i]);
        double media_resipipe = media(resipipe[i]);

        cout << "  Config " << i + 1
             << " | OpenMPI media: " << media_openmpi
             << " | ResiPipe media: " << media_resipipe << "\n";

        if(media_openmpi > best_media_openmpi) {
            best_media_openmpi = media_openmpi;
            best_config_openmpi = i;
        }

        if(media_resipipe > best_media_resipipe) {
            best_media_resipipe = media_resipipe;
            best_config_resipipe = i;
        }
    }

    cout << "\n  Melhor OpenMPI:  Config " << best_config_openmpi + 1
         << "  Media: " << best_media_openmpi << "\n";

    cout << "  Melhor ResiPipe: Config " << best_config_resipipe + 1
         << "  Media: " << best_media_resipipe << "\n";

    double dr = (best_media_resipipe - best_media_openmpi) / best_media_openmpi * 100.0;

    cout << "  Diferença relativa: " << dr << "%\n";
    cout << "------------------------------------\n\n";

    best_media_omp.push_back(best_media_openmpi);
    best_media_res.push_back(best_media_resipipe);
}

int main() {

    vector<double> best_media_omp;
    vector<double> best_media_res;

    run("FD", fd_openmpi, fd_resipipe, best_media_omp, best_media_res);
    run("SA", sa_openmpi, sa_resipipe, best_media_omp, best_media_res);
    run("SD", sd_openmpi, sd_resipipe, best_media_omp, best_media_res);
    run("TM", tm_openmpi, tm_resipipe, best_media_omp, best_media_res);

    double mg_openmpi = media_geometrica(best_media_omp);
    double mg_resipipe = media_geometrica(best_media_res);

    double dr_mg = (mg_resipipe - mg_openmpi) / mg_openmpi * 100;

    cout << "\nMédia geométrica OpenMPI: " << mg_openmpi << "\n";
    cout << "Média geométrica ResiPipe: " << mg_resipipe << "\n";
    cout << "Diferença relativa da MG: " << dr_mg << "%\n";
}