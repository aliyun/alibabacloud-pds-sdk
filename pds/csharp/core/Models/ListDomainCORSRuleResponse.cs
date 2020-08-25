// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * list domain cors response
     */
    public class ListDomainCORSRuleResponse : TeaModel {
        /// <summary>
        /// cors rule 列表
        /// </summary>
        [NameInMap("cors_rule_list")]
        [Validation(Required=false)]
        public List<CorsRule> CorsRuleList { get; set; }

        /// <summary>
        /// Domain ID
        /// </summary>
        [NameInMap("domain_id")]
        [Validation(Required=false)]
        public string DomainId { get; set; }

    }

}
