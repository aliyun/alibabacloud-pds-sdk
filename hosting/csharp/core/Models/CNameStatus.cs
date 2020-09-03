// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 
     */
    public class CNameStatus : TeaModel {
        /// <summary>
        /// binding state
        /// </summary>
        [NameInMap("bingding_state")]
        [Validation(Required=true)]
        public string BingdingState { get; set; }

        /// <summary>
        /// legal state
        /// </summary>
        [NameInMap("legal_state")]
        [Validation(Required=true)]
        public string LegalState { get; set; }

        /// <summary>
        /// remark
        /// </summary>
        [NameInMap("remark")]
        [Validation(Required=true)]
        public string Remark { get; set; }

    }

}
