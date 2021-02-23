// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 
     */
    public class GetSubdomainRequest : TeaModel {
        [NameInMap("headers")]
        [Validation(Required=false)]
        public Dictionary<string, string> Headers { get; set; }

        /// <summary>
        /// 用以唯一标识subdomain
        /// </summary>
        [NameInMap("subdomain_id")]
        [Validation(Required=true)]
        public string SubdomainId { get; set; }

    }

}
