<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * GetOfficeEditUrlWatermark 水印配置.
 */
class GetOfficeEditUrlWatermark extends Model
{
    /**
     * @description FillStyle
     *
     * @var string
     */
    public $fillstyle;

    /**
     * @description Font
     *
     * @var string
     */
    public $font;

    /**
     * @description Horizontal
     *
     * @var int
     */
    public $horizontal;

    /**
     * @description Rotate
     *
     * @var float
     */
    public $rotate;

    /**
     * @description Type
     *
     * @var int
     */
    public $type;

    /**
     * @description Value
     *
     * @var string
     */
    public $value;

    /**
     * @description Vertical
     *
     * @var int
     */
    public $vertical;
    protected $_name = [
        'fillstyle'  => 'fillstyle',
        'font'       => 'font',
        'horizontal' => 'horizontal',
        'rotate'     => 'rotate',
        'type'       => 'type',
        'value'      => 'value',
        'vertical'   => 'vertical',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->fillstyle) {
            $res['fillstyle'] = $this->fillstyle;
        }
        if (null !== $this->font) {
            $res['font'] = $this->font;
        }
        if (null !== $this->horizontal) {
            $res['horizontal'] = $this->horizontal;
        }
        if (null !== $this->rotate) {
            $res['rotate'] = $this->rotate;
        }
        if (null !== $this->type) {
            $res['type'] = $this->type;
        }
        if (null !== $this->value) {
            $res['value'] = $this->value;
        }
        if (null !== $this->vertical) {
            $res['vertical'] = $this->vertical;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return GetOfficeEditUrlWatermark
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['fillstyle'])) {
            $model->fillstyle = $map['fillstyle'];
        }
        if (isset($map['font'])) {
            $model->font = $map['font'];
        }
        if (isset($map['horizontal'])) {
            $model->horizontal = $map['horizontal'];
        }
        if (isset($map['rotate'])) {
            $model->rotate = $map['rotate'];
        }
        if (isset($map['type'])) {
            $model->type = $map['type'];
        }
        if (isset($map['value'])) {
            $model->value = $map['value'];
        }
        if (isset($map['vertical'])) {
            $model->vertical = $map['vertical'];
        }

        return $model;
    }
}
