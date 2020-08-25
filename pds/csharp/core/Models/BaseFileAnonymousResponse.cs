// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * list_file_by_anonymous base response
     */
    public class BaseFileAnonymousResponse : TeaModel {
        /// <summary>
        /// file_id
        /// </summary>
        [NameInMap("file_id")]
        [Validation(Required=false, MaxLength=50, Pattern="[a-z0-9]{1,50}")]
        public string FileId { get; set; }

        /// <summary>
        /// name
        /// </summary>
        [NameInMap("name")]
        [Validation(Required=false, Pattern="[a-zA-Z0-9.-]{1,1000}")]
        public string Name { get; set; }

        /// <summary>
        /// size, type=file时才有效
        /// </summary>
        [NameInMap("size")]
        [Validation(Required=false)]
        public long Size { get; set; }

        /// <summary>
        /// thumbnail
        /// </summary>
        [NameInMap("thumbnail")]
        [Validation(Required=false)]
        public string Thumbnail { get; set; }

        /// <summary>
        /// type
        /// </summary>
        [NameInMap("type")]
        [Validation(Required=false)]
        public string Type { get; set; }

        /// <summary>
        /// updated_at
        /// </summary>
        [NameInMap("updated_at")]
        [Validation(Required=false)]
        public string UpdatedAt { get; set; }

    }

}
