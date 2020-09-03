// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * Pre hash check Response
     */
    public class PreHashCheckSuccessResponse : TeaModel {
        /// <summary>
        /// code
        /// </summary>
        [NameInMap("code")]
        [Validation(Required=false)]
        public string Code { get; set; }

        /// <summary>
        /// file_name
        /// </summary>
        [NameInMap("file_name")]
        [Validation(Required=false)]
        public string FileName { get; set; }

        /// <summary>
        /// message
        /// </summary>
        [NameInMap("message")]
        [Validation(Required=false)]
        public string Message { get; set; }

        /// <summary>
        /// parent_file_id
        /// </summary>
        [NameInMap("parent_file_id")]
        [Validation(Required=true, MaxLength=50, Pattern="[a-z0-9]{1,50}")]
        public string ParentFileId { get; set; }

        /// <summary>
        /// pre_hash
        /// </summary>
        [NameInMap("pre_hash")]
        [Validation(Required=false)]
        public string PreHash { get; set; }

    }

}
