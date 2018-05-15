#include <iostream>
#include <fstream>
#include <string>
#include <curl/curl.h>

using namespace std;

static size_t WriteCallback(void *contents, size_t size, size_t nmemb, void *userp)
{
   ((string*)userp)->append((char*)contents, size * nmemb);
   return size * nmemb;
}

void indent(string &s){
    string tmp;
    for(unsigned int i=0; i<s.size(); i++){
        if(s.at(i)==','){
            tmp = tmp + "\n"; 
            if(s.at(i+1)!='{'){
                tmp = tmp +"\t";
            }
        }
        tmp = tmp + s.at(i);
    }
    s = tmp;
}

int main(int argc, char* argv[]){

    CURL *curl;
    CURLcode res;
    string output;
    string url;

    if(argc!=4){
        if(argc==2 && argv[1]==string("-h")){
            cout << endl 
                 << "This programs aims to retrive prices and volumes of the most popular cryptocurrencies," << endl
                 << "this is done by using https://www.cryptocompare.com/ APIs and saving the data on a json file." << endl
                 << "To achive this, you must call the program, and passing it the crypto you want the data of," << endl 
                 << "also you need to pass the time interval you are interested in, m for minutes, h for hours, d for days" << endl << endl
                 << "example --> ./crypto-fetcher BTC EUR m" << endl << endl
                 << "This way you will obtain bitcoin/euros price updated once per minute" << endl
                 << "To get the full coin list, please visit: https://www.cryptocompare.com/api/data/coinlist/" << endl
                 << "Remember that cryptocompare lets you fetch the prices up to 'only' 6000 times per hour" << endl << endl
                 << "This tool is released under GNU GPL Version 3" << endl
                 << endl;
                 return 0;
        }
        else{
            cout << "If you don't know how to use this program, check for the help with -h" << endl;
            return 0;
        }
    }
    else{
        string from = argv[1];
        string to = argv[2];
        switch(*argv[3]){
            case 'm':
                url="https://min-api.cryptocompare.com/data/histominute?fsym=" +
                 from + "&tsym=" + to +
                 "&limit=60&aggregate=3&e=CCCAGG";
            break;
            case 'h':
                url="https://min-api.cryptocompare.com/data/histohour?fsym=" +
                 from + "&tsym=" + to +
                 "&limit=60&aggregate=3&e=CCCAGG";
            break;
            case 'd':
                url="https://min-api.cryptocompare.com/data/histoday?fsym=" + 
                 from + "&tsym=" + to +
                 "&limit=60&aggregate=3&e=CCCAGG";
            break;
            default:
                cout << "Char not known" << endl;
            return 0;
            break;
        }
    }

    curl = curl_easy_init();
    if(curl) {
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &output);
        res = curl_easy_perform(curl);
        curl_easy_cleanup(curl);
        curl_global_cleanup();
    }

    ofstream outfile ("crypto.json");
    indent(output);
    outfile << output;
    outfile.close();
    cout << "Data correctly written on crypto.json" << endl;

    return 0;
}
