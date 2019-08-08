import { NgModule } from '@angular/core';
import { TriagemComponent } from './components/triagem/triagem.component';
import { TriagemRoutingModule } from './triagem-routing.module';
import { TriagemService } from './components/services/triagem.service';
import { CommonModule } from '@angular/common';
import { SintomasComponent } from './components/sintomas/sintomas.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ClassificacaoManchesterComponent } from './components/classificacao-manchester/classificacao-manchester.components';

@NgModule({
    declarations: [
        TriagemComponent,
        SintomasComponent
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
        ReactiveFormsModule
    ],
  })
  export class TriagemModule { }
  