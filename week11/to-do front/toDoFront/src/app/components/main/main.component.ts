import { AfterViewInit, Component, OnInit, ViewChild } from '@angular/core';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit, AfterViewInit {

  @ViewChild('counting') counter;
  i:any;

  @ViewChild('formInput') note;  //note_text
  @ViewChild('contBlock') block;
 
  @ViewChild('noteBlock') divInit;
  divCurr:any;
  par:any;
  checkBox:any;

  constructor() { 

  }

  ngOnInit() {

  }

  ngAfterViewInit() {}

  CreateDiv() {
  	
  	this.i = this.counter.nativeElement.innerHtml; //Counter of id's
  	var a = this.divInit.nativeElement.cloneNode(true);
  	a.nativeElement.style.display = "block";

  	this.par = this.divCurr.nativeElement.firstChild.children[1];
  	this.par.nativeElement.innerHtml = this.note.nativeElement.value;
  	this.par.nativeElement.id = this.par.nativeElement.id + this.i;

  	this.checkBox = this.divCurr.nativeElement.firstChild.firstChild;
  	this.checkBox.nativeElement.id = this.i;

  	this.divCurr.nativeElement.id = this.divCurr.nativeElement.id + 1;
  	this.block.nativeElement.appendChild(this.divCurr);

  	this.i = Number(this.i);
  	this.counter.nativeElement.innerHtml = this.i + 1;
  }



}
