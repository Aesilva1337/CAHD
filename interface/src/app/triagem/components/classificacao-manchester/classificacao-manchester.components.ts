import { Component, OnInit } from '@angular/core';
import { TriagemService } from '../services/triagem.service';
import { DiagnosticoModel } from '../models/components/diagnostico.model';
import { EClassificacaoManchester } from '../models/enum/classificacao-manchester.enum';
import { ClassificacaoManchesterModel } from '../models/components/classificacao-manchester.model';
import { faExclamation } from '@fortawesome/free-solid-svg-icons';
@Component({
    selector: 'app-classificacao-manchester',
    templateUrl: './classificacao-manchester.component.html',
    styleUrls: ['./classificacao-manchester.component.scss']
  })
  export class ClassificacaoManchesterComponent implements OnInit {
    constructor(
      private triagemService: TriagemService,
    ) {
    }
    faExclamation = faExclamation;
    private classificacao: ClassificacaoManchesterModel;

    async ngOnInit() {
        this.definirClassificacao(EClassificacaoManchester.Emergencia)
    }
    
    async definirClassificacao(classificacao: EClassificacaoManchester) {        
        const response = await this.triagemService.ObterInformacoesClassificacaoManchester(classificacao);
        this.classificacao = response.data;
    }
  }