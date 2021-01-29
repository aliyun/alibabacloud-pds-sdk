// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * Remove story images response
     */
    public class RemoveStoryImagesResponse : TeaModel {
        /// <summary>
        /// drive_id
        /// </summary>
        [NameInMap("drive_id")]
        [Validation(Required=false)]
        public string DriveId { get; set; }

        /// <summary>
        /// file_ids
        /// </summary>
        [NameInMap("file_ids")]
        [Validation(Required=false)]
        public List<string> FileIds { get; set; }

        [NameInMap("results")]
        [Validation(Required=false)]
        public List<RemoveStoryImagesResultItem> Results { get; set; }

        /// <summary>
        /// story_id
        /// </summary>
        [NameInMap("story_id")]
        [Validation(Required=false)]
        public string StoryId { get; set; }

        /// <summary>
        /// success_file_ids
        /// </summary>
        [NameInMap("success_file_ids")]
        [Validation(Required=false)]
        public List<string> SuccessFileIds { get; set; }

    }

}
