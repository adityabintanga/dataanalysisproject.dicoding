import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

day_df = pd.read_csv("https://raw.githubusercontent.com/adityabintanga/dataanalysisproject.dicoding/main/day.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/adityabintanga/dataanalysisproject.dicoding/main/hour.csv")

def main():
    st.title("Bike Sharing Analysis")
    st.caption('from: Bike Sharing Dataset.(2013)')  
    st.write(
        """Sistem berbagi sepeda adalah generasi baru dari penyewaan sepeda tradisional di mana
        seluruh proses mulai dari keanggotaan, penyewaan, dan pengembalian sepeda menjadi 
        otomatis. Melalui sistem ini, pengguna dapat dengan mudah menyewa sepeda dari posisi 
        tertentu dan mengembalikannya di posisi lain. Saat ini, terdapat lebih dari 500 program 
        berbagi sepeda di seluruh dunia yang terdiri dari lebih dari 500 ribu sepeda. Saat ini, terdapat 
        minat yang besar terhadap sistem ini karena peran penting mereka dalam masalah lalu lintas, 
        lingkungan dan kesehatan. 
        Terlepas dari aplikasi dunia nyata yang menarik dari sistem berbagi sepeda, karakteristik data 
        yang dihasilkan oleh sistem ini membuatnya menarik untuk penelitian. Berbeda dengan 
        layanan transportasi lain seperti bus atau kereta bawah tanah, durasi perjalanan, posisi 
        keberangkatan dan kedatangan secara eksplisit dicatat dalam sistem ini. Fitur ini mengubah 
        sistem berbagi sepeda menjadi jaringan sensor virtual yang dapat digunakan untuk merasakan 
        mobilitas di kota. Dengan demikian, diharapkan sebagian besar kejadian penting di kota 
        dapat dideteksi melalui pemantauan data ini."""
    )
    
    with st.sidebar:
        st.text('Additional Information')

        st.write(pd.DataFrame({
        'Season Number': [1, 2, 3, 4],
        'Season Name': ['Springer', 'Summer', 'fall', 'winter'],
        }))

        st.write(pd.DataFrame({
        'Weather Number': [1, 2, 3, 4],
        'Weather Name': ['Clear, Few clouds, Partly cloudy, Partly cloudy',
                         'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist',
                         'Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds',
                         'Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog'],
        }))        

    tab1, tab2 = st.tabs(["Seasonal and Weather Analysis", "Monthly and Hourly Analysis"])
    
    with tab1:
        st.subheader("Seasonal and Weather Analysis")
        col1, col2= st.columns(2)
        
        with col1:
            seasonal_averages = day_df.groupby(by="season").agg({
                "casual": "mean",
                "registered": "mean",
                "cnt": "mean"
            }).reset_index()

            plt.figure(figsize=(12, 8))
            bar_width = 0.25
            r1 = np.arange(len(seasonal_averages['season']))
            r2 = [x + bar_width for x in r1]
            r3 = [x + bar_width for x in r2]

            plt.bar(r1, seasonal_averages['casual'], color='yellow', width=bar_width, edgecolor='yellow', label='Casual')
            plt.bar(r2, seasonal_averages['registered'], color='orange', width=bar_width, edgecolor='orange', label='Registered')
            plt.bar(r3, seasonal_averages['cnt'], color='red', width=bar_width, edgecolor='red', label='Total Count (cnt)')

            plt.title('Average Users by Season (data per day)')
            plt.xlabel('Season')
            plt.xticks([r + bar_width for r in range(len(seasonal_averages['season']))], seasonal_averages['season'])
            plt.ylabel('Average Users')
            plt.legend()
            st.pyplot(plt)

        with col2:
            seasonal_averages = hour_df.groupby(by="season").agg({
                "casual": "mean",
                "registered": "mean",
                "cnt": "mean"
            }).reset_index()

            plt.figure(figsize=(12, 8))
            bar_width = 0.25
            r1 = np.arange(len(seasonal_averages['season']))
            r2 = [x + bar_width for x in r1]
            r3 = [x + bar_width for x in r2]

            plt.bar(r1, seasonal_averages['casual'], color='yellow', width=bar_width, edgecolor='yellow', label='Casual')
            plt.bar(r2, seasonal_averages['registered'], color='orange', width=bar_width, edgecolor='orange', label='Registered')
            plt.bar(r3, seasonal_averages['cnt'], color='red', width=bar_width, edgecolor='red', label='Total Count (cnt)')

            plt.title('Average Users by Season (data per hour)')
            plt.xlabel('Season')
            plt.xticks([r + bar_width for r in range(len(seasonal_averages['season']))], seasonal_averages['season'])
            plt.ylabel('Average Users')
            plt.legend()
            st.pyplot(plt)

        st.write(
            """Berdasarkan grafik Rata-rata users berdasarkan musim dengan menggunakan data day.csv dan hour.csv, terlihat bahwa 
            baik casual users maupun registered users melakukan rental sepeda paling banyak di musim ketiga yaitu musim gugur (fall) 
            dan paling sedikit di musim pertama yaitu musim semi (springer)"""
        )

        col3, col4= st.columns(2)
        with col3:
            weather_averages = day_df.groupby(by="weathersit").agg({
                "casual": "mean",
                "registered": "mean",
                "cnt": "mean"
            }).reset_index()

            plt.figure(figsize=(12, 8))

            bar_width = 0.25

            r1 = np.arange(len(weather_averages['weathersit']))
            r2 = [x + bar_width for x in r1]
            r3 = [x + bar_width for x in r2]

            plt.bar(r1, weather_averages['casual'], color='skyblue', width=bar_width, edgecolor='skyblue', label='Casual')
            plt.bar(r2, weather_averages['registered'], color='blue', width=bar_width, edgecolor='blue', label='Registered')
            plt.bar(r3, weather_averages['cnt'], color='darkblue', width=bar_width, edgecolor='darkblue', label='Total Count (cnt)')

            plt.title('Average Users by Weather Situation (data per day)')
            plt.xlabel('Weather Situation')
            plt.xticks([r + bar_width for r in range(len(weather_averages['weathersit']))], weather_averages['weathersit'])
            plt.ylabel('Average Users')

            plt.legend()
            st.pyplot(plt)

        with col4:
            weather_averages = hour_df.groupby(by="weathersit").agg({
                "casual": "mean",
               "registered": "mean",
                "cnt": "mean"
            }).reset_index()

            plt.figure(figsize=(12, 8))

            bar_width = 0.25

            r1 = np.arange(len(weather_averages['weathersit']))
            r2 = [x + bar_width for x in r1]
            r3 = [x + bar_width for x in r2]

            plt.bar(r1, weather_averages['casual'], color='skyblue', width=bar_width, edgecolor='skyblue', label='Casual')
            plt.bar(r2, weather_averages['registered'], color='blue', width=bar_width, edgecolor='blue', label='Registered')
            plt.bar(r3, weather_averages['cnt'], color='darkblue', width=bar_width, edgecolor='darkblue', label='Total Count (cnt)')

            plt.title('Average Users by Weather Situation (data per hour)')
            plt.xlabel('Weather Situation')
            plt.xticks([r + bar_width for r in range(len(weather_averages['weathersit']))], weather_averages['weathersit'])
            plt.ylabel('Average Users')

            plt.legend()
            st.pyplot(plt)

        st.write(
            """Berdasarkan grafik Rata-rata users berdasarkan cuaca dengan menggunakan data day.csv 
            dan hour.csv terlihat bahwa baik casual users maupun registered users melakukan rental 
            sepeda paling banyak pada saat cuaca pertama yaitu Clear, Few clouds, Partly cloudy, Partly 
            cloudy dan paling sedikit pada saat cuaca ketiga yaitu Light Snow, Light Rain + 
            Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
            """
        )

    with tab2:
        st.subheader("Monthly and Hourly Analysis")

        monthly_averages = day_df.groupby(by="mnth").agg({
            "casual": "mean",
            "registered": "mean",
            "cnt": "mean"
        }).reset_index()

        plt.figure(figsize=(12, 8))

        plt.plot(monthly_averages['mnth'], monthly_averages['casual'], color='yellow', marker='o', label='Casual')
        plt.plot(monthly_averages['mnth'], monthly_averages['registered'], color='orange', marker='s', label='Registered')
        plt.plot(monthly_averages['mnth'], monthly_averages['cnt'], color='red', marker='^', label='Total Count (cnt)')

        plt.title('Average Monthly Users')
        plt.xlabel('Month')
        plt.xticks(monthly_averages['mnth'])  # Asumsikan 'mnth' adalah 1-12 atau sesuai dengan data Anda
        plt.ylabel('Average Users')

        plt.legend()
        st.pyplot(plt)

        st.write(
            """Beradasarkan grafik Rata-rata users tiap bulan dengan menggunakan data day.csv, terlihat 
            bahwa baik casual users maupun registered users mangalami peningkatan yang cukup 
            signifikan dari bulan ke-3 (maret) hingga bulan ke-6 (juni). Dan akan mengalami penurunan 
            mulai dari bulan ke-9 (September) hingga bulan ke-12 (desember). Hal ini tentunya 
            dipengaruhi oleh banyak faktor, diantaranya yaitu musim, cuaca, hari kerja dan hari 
            libur/weekend"""
        )


        hourly_averages = hour_df.groupby(by="hr").agg({
            "casual": "mean",
            "registered": "mean",
            "cnt": "mean"
        }).reset_index()

        plt.figure(figsize=(14, 8))

        plt.plot(hourly_averages['hr'], hourly_averages['casual'], color='skyblue', marker='o', label='Casual', linestyle='-')
        plt.plot(hourly_averages['hr'], hourly_averages['registered'], color='blue', marker='s', label='Registered', linestyle='-')
        plt.plot(hourly_averages['hr'], hourly_averages['cnt'], color='darkblue', marker='^', label='Total Count (cnt)', linestyle='-')

        plt.title('Average Users by Hour')
        plt.xlabel('Hour of the Day')
        plt.xticks(hourly_averages['hr'])
        plt.ylabel('Average Users')

        plt.grid(True, which='both', linestyle='--', linewidth=0.5)

        plt.legend()
        st.pyplot(plt)

        st.write(
            """Beradasarkan grafik Rata-rata users tiap jam dengan menggunakan data hour.csv, terlihat 
            bahwa untuk casual users mengalami peningkatan pada jam mulai beraktivitas atau jam 
            berangkat kerja mulai dari pukul 08.00 hingga pukul 17.00. Setelah itu casual users 
            mengalami penurunan hingga jam 23.00
            Sementara itu, untuk registered users mengalami peningkatan yang siginifikan pada jam 
            mulai beraktivitas atau jam berangkat kerja mulai pukul 06.00 hingga mencapai puncaknya 
            pada pukul 08.00. Setelah itu, registered users mengalami penurunan dan mulai mengalami 
            peningkatan kembali pada jam pulang kerja mulai pukul 16.00 hingga mencapai puncaknya 
            pada pukul 17.00. Setelah itu registered users mengalami penurunan hingga jam 23.00"""
        )

if __name__ == "__main__":
    main()
