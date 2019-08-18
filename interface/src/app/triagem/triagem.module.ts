import { NgModule } from '@angular/core';
import { TriagemComponent } from './components/triagem/triagem.component';
import { TriagemRoutingModule } from './triagem-routing.module';
import { TriagemService } from './components/services/triagem.service';
import { CommonModule } from '@angular/common';
import { SintomasComponent } from './components/sintomas/sintomas.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ClassificacaoManchesterComponent } from './components/classificacao-manchester/classificacao-manchester.components';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

@NgModule({
    declarations: [
        TriagemComponent,
        SintomasComponent,
        ClassificacaoManchesterComponent
    ],
    entryComponents: [
        TriagemComponent
    ],
    providers: [
        TriagemService
    ],
    imports: [
        TriagemRoutingModule,
        CommonModule,
        FormsModule,
        ReactiveFormsModule,
        FontAwesomeModule
    ],
  })
  export class TriagemModule { }
  