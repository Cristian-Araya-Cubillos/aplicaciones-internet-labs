import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  genres: any[] = [];
  selectedGenre: string = '';
  responseData: any[] = [];

  constructor(private http: HttpClient) {
    this.getGenres();
  }

  getGenres() {
    this.http.get('http://api.filmon.com/api/vod/genres')
      .subscribe((data: any) => {
        console.log('API Response:', data); 
        this.genres = data.response.map((genre: any) => genre.slug);
        console.log('Genres:', this.genres);
      });
  }

  onGenreSelected(event: any) {
    this.selectedGenre = event.target.value;

    if (this.selectedGenre) {
      this.http.get(`http://api.filmon.com/api/vod/search?genre=${this.selectedGenre}`)
        .subscribe((data: any) => {
          console.log('API Search Response:', data);
          this.responseData = data.response;
          console.log('Response Data:', this.responseData);
        });
    }
  }
}
