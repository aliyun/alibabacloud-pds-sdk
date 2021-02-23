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
    public class BaseGroupIDRequest : TeaModel {
        /// <summary>
        /// group id
        /// </summary>
        [NameInMap("group_id")]
        [Validation(Required=false)]
        public string GroupId { get; set; }

        /// <summary>
        /// subdomain id
        /// </summary>
        [NameInMap("subdomain_id")]
        [Validation(Required=false)]
        public string SubdomainId { get; set; }

    }

}
