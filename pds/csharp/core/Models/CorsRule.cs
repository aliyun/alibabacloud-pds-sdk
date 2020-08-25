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
    public class CorsRule : TeaModel {
        /// <summary>
        /// AllowedHeader
        /// </summary>
        [NameInMap("allowed_header")]
        [Validation(Required=false)]
        public List<string> AllowedHeader { get; set; }

        /// <summary>
        /// AllowedMethod
        /// </summary>
        [NameInMap("allowed_method")]
        [Validation(Required=false)]
        public List<string> AllowedMethod { get; set; }

        /// <summary>
        /// AllowedOrigin
        /// </summary>
        [NameInMap("allowed_origin")]
        [Validation(Required=false)]
        public List<string> AllowedOrigin { get; set; }

        /// <summary>
        /// ExposeHeader
        /// </summary>
        [NameInMap("expose_header")]
        [Validation(Required=false)]
        public List<string> ExposeHeader { get; set; }

        /// <summary>
        /// MaxAgeSeconds
        /// </summary>
        [NameInMap("max_age_seconds")]
        [Validation(Required=false)]
        public long MaxAgeSeconds { get; set; }

    }

}
