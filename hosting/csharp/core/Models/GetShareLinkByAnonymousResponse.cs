// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * get_share_link_by_anonymous response
     */
    public class GetShareLinkByAnonymousResponse : TeaModel {
        /// <summary>
        /// creator_id
        /// </summary>
        [NameInMap("creator_id")]
        [Validation(Required=false)]
        public string CreatorId { get; set; }

        /// <summary>
        /// creator_name
        /// </summary>
        [NameInMap("creator_name")]
        [Validation(Required=false)]
        public string CreatorName { get; set; }

        /// <summary>
        /// expiration
        /// </summary>
        [NameInMap("expiration")]
        [Validation(Required=false)]
        public string Expiration { get; set; }

        /// <summary>
        /// updated_at
        /// </summary>
        [NameInMap("updated_at")]
        [Validation(Required=false)]
        public string UpdatedAt { get; set; }

    }

}
