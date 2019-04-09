import { AfterViewInit, Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
 
  options:string[] = [];

  constructor() { 

  }

  ngOnInit() {

  }

  addOpt(option){
  	this.options.unshift(option);
  	return false;
  }

  deleteOpt(option){
  	for(let i = 0; i < this.options.length; i++){
  		if(this.options[i] == option){
  			this.options.splice(i, 1);
  			break;
  		}
  	}
  }

}
