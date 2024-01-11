<template>
  <v-app>
    <v-main>
      <v-container>
        <v-card class="text-center">
          <v-card-title class="text-h5">Weather App</v-card-title>
          <v-card-subtitle>
            Check the current temperature and humidity for your city.
          </v-card-subtitle>
          <v-card-text>
            <v-text-field
              v-model="city"
              label="Enter a city"
              outlined
              dense
              class="mb-4"
            ></v-text-field>
            <v-btn @click="getWeather" color="primary">Check Weather</v-btn>
            <v-alert v-if="weather" type="info" class="mt-4" variant="outlined">
              <span class="text-h5">Current weather information for {{ cityResult }}:</span>
              <div class="display-1" :style="{ color: temperatureColor }">
                Temperature: {{ weather.temperature }}°C
              </div>
              <div>Humidity: {{ weather.humidity }}%</div>
            </v-alert>
          </v-card-text>
        </v-card>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      city: '',
      weather: null,
      cityResult: ''
    };
  },
  computed: {
    temperatureColor() {
      if (!this.weather) return '#000';
      const temperature = this.weather.temperature;
      if (temperature < 10) return '#3498db'; // Blue for cold temperatures
      if (temperature >= 10 && temperature < 20) return '#f1c40f'; // Yellow for mild temperatures
      return '#e74c3c'; // Red for warm temperatures
    }
  },
  methods: {
    async getWeather() {
      try {
        const response = await axios.get(`https://api.weatherapi.com/v1/current.json?key=888c3e1a62a748fc83a94130231912&q=${this.city}`);
        this.weather = {
          temperature: response.data.current.temp_c,
          humidity: response.data.current.humidity
        };
        cityResult = city;
      } catch (error) {
        console.error(error);
      }
    }
  }
};
</script>

<style>
.text-center {
  text-align: center;
}
</style>
