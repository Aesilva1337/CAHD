import { NgModule } from '@angular/core';
import { TriagemComponent } from './components/triagem/triagem.component';
import { TriagemRoutingModule } from './triagem-routing.module';
import { TriagemService } from './components/services/triagem.service';
import { CommonModule } from '@angular/common';

@NgModule({
    declarations: [
        TriagemComponent
    ],
    entryComponents: [TriagemComponent],
    providers: [
        TriagemService
    ],
    imports: [
        TriagemRoutingModule,
        CommonModule,
    ],
  })
  export class TriagemModule { }
  