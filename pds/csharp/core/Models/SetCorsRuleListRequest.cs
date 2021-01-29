// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * list cors rule request
     */
    public class SetCorsRuleListRequest : TeaModel {
        /// <summary>
        /// cors rule list
        /// </summary>
        [NameInMap("cors_rule_list")]
        [Validation(Required=true)]
        public List<CorsRule> CorsRuleList { get; set; }

        /// <summary>
        /// domain ID
        /// </summary>
        [NameInMap("domain_id")]
        [Validation(Required=true)]
        public string DomainId { get; set; }

    }

}
